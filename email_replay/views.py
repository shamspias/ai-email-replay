from rest_framework import viewsets, permissions
from .serializers import GetEmailSerializers
from .models import EmailWithReplays


class EmailReplayGenViewSet(viewsets.ModelViewSet):
    """ViewSet for generated email replay"""

    queryset = EmailWithReplays.objects.all()
    serializer_class = GetEmailSerializers
    permission_classes = [permissions.AllowAny, ]
