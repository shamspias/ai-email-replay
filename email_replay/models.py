from django.db import models


class EmailWithReplays(models.Model):
    """
    Email model to store email and choices replay and other options as well
    """
    email_subject = models.CharField(max_length=250, blank=True, null=True)
    email_body = models.TextField(blank=True, null=True)
    replay = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.email_body:
            return self.email_body[:20]
        else:
            return "Email with Replay"
