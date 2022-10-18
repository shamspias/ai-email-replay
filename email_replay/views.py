from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializers, GetEmailReplaySerializers
from .models import EmailWithReplays
from .task import generate_customer_replay


class EmailReplayGenViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """and get replay """

    queryset = EmailWithReplays.objects.all()
    serializer_class = EmailSerializers
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        my_string = ""
        for i in data['body']:
            my_string += i['actor'] + ":\n" + i['body'] + "\n"
        context = generate_customer_replay(data['subject'], my_string)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return Response(context, status=status.HTTP_201_CREATED, )
