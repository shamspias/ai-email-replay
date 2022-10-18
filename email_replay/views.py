from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import EmailSerializers, GetEmailReplaySerializers
from .models import EmailWithReplays


class EmailReplayGenViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """and get replay """

    queryset = EmailWithReplays.objects.all()
    serializers = {'default': EmailSerializers, 'replay': GetEmailReplaySerializers}
    permissions = {'default': (permissions.AllowAny,), }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='replay', url_name='replay')
    def get_email_replay(self, instance):
        try:
            return Response(GetEmailReplaySerializers(self.request.user, context={'request': self.request}).data,
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wrong token' + e}, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['post'], url_path='data', url_name='data')
    # def post_email_data(self, instance):
    #     try:
    #         return Response(EmailSerializers(self.request.user, context={'request': self.request}).data,
    #                         status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({'error': 'Wrong token' + e}, status=status.HTTP_400_BAD_REQUEST)
