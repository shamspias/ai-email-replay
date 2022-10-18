from celery import shared_task
from django.conf import settings

import openai


@shared_task(name='GenerateEmailReplay')
def generate_email_replay(prompt):
    """
    Method to generate email replay from OpenAI using GPT3
    """
    openai.api_key = settings.OPEN_AI_KEY

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Suggest 4 short email replay from this email context\n {}\n\n1.".format(prompt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    my_text = response['choices'][0]['text'].split("\n")
    context = {
        'data': [word_value[3:] if word_value[0] != " " else word_value[4:] if i != 0 else word_value[1:] for
                 i, word_value in enumerate(my_text) if word_value != ""]
    }
    return context


@shared_task(name='ReplayCustomer')
def generate_customer_replay(subject, prompt):
    """
    Method to generate email replay from OpenAI using GPT3
    """
    openai.api_key = settings.OPEN_AI_KEY

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Give 4 answers suggestions about {}, based on replay from this conversation \n {}\n\nAgent:\n1.\n".format(
            subject, prompt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    my_text = response['choices'][0]['text'].split("\n")

    new_text = []
    for i, word in enumerate(my_text):
        if len(word) > 4:
            new_text.append(word)
    context = {
        'data': new_text
    }
    return context
