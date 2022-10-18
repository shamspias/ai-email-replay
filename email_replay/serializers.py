from rest_framework import serializers
from .models import EmailWithReplays, EmailBody, EmailReplay


class EmailBodySerializers(serializers.ModelSerializer):
    """
    Serializer class to get email
    """

    class Meta:
        model = EmailBody
        fields = [
            'actor',
            'body',
        ]


class EmailReplaySerializers(serializers.ModelSerializer):
    """
    Serializer class to get email
    """

    class Meta:
        model = EmailReplay
        fields = [
            'title',
            'body',
        ]


class EmailSerializers(serializers.ModelSerializer):
    """
    Serializer class to get email
    """
    body = EmailBodySerializers(read_only=True)
    body_id = serializers.PrimaryKeyRelatedField(
        queryset=EmailBody.objects.all(), source='body', write_only=True)

    class Meta:
        model = EmailWithReplays
        fields = [
            'subject',
            'body',
            'body_id',

        ]


class GetEmailReplaySerializers(serializers.ModelSerializer):
    """
    Serializer class to get email
    """
    replay = EmailReplaySerializers(read_only=True)
    replay_id = serializers.PrimaryKeyRelatedField(
        queryset=EmailReplay.objects.all(), source='body', write_only=True)

    class Meta:
        model = EmailWithReplays
        fields = [
            'replay',
            'replay_id',
        ]
