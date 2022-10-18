from rest_framework import serializers
from .models import EmailWithReplays


class GetEmailSerializers(serializers.ModelSerializer):
    """
    Serializer class to get email
    """

    class Meta:
        model = EmailWithReplays
        fields = [
            'email_subject',
            'email_body',
        ]
