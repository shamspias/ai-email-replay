from django.contrib import admin
from .models import EmailBody, EmailReplay, EmailWithReplays

admin.site.register(EmailBody)
admin.site.register(EmailReplay)
admin.site.register(EmailWithReplays)
