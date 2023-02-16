from django.urls import path
from .views import *


urlpatterns = [
    path('users/', BotUserListCreateAPIView.as_view()),
    path('messages/', MessagesHistoryListCreateAPIView.as_view()),
]

