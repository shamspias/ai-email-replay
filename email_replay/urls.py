from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EmailReplayGenViewSet
)

email_replay_router = DefaultRouter()
email_replay_router.register('email', EmailReplayGenViewSet)
