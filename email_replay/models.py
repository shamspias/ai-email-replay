from django.db import models


class EmailBody(models.Model):
    """
    Email body Model
    """
    actor = models.CharField(max_length=40, blank=True, null=True)
    body = models.TextField(blank=True, null=True)


class EmailReplay(models.Model):
    """
    Email Replay Model
    """
    title = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField(blank=True, null=True)


class EmailWithReplays(models.Model):
    """
    Email model to store email and choices replay and other options as well
    """
    subject = models.CharField(max_length=250, blank=True, null=True)
    body = models.ManyToManyField(EmailBody, related_name="email_body")
    replay = models.ManyToManyField(EmailReplay, related_name="email_replay")

    def __str__(self):
        if self.subject:
            return self.subject
        else:
            return "No Subject"
