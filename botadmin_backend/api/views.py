from rest_framework import generics
from customers.models import MessagesHistory, BotUser
from .serializers import MessagesHistorySerializer, BotUserSerializer


class BotUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class MessagesHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = MessagesHistory.objects.all()
    serializer_class = MessagesHistorySerializer

    def perform_create(self, serializer):
        telegram_user_id = self.request.data.get('telegram_user_id')
        bot_user, _ = BotUser.objects.get_or_create(telegram_user_id=telegram_user_id)
        serializer.save(bot_user=bot_user)
