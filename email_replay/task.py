from celery import shared_task


@shared_task(name='GenerateEmailReplay')
def generate_email_replay(subject, to, default_from, email_html_message):
    """
    Method to generate email replay from OpenAI using GPT3
    """
    pass
