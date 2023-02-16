from rest_framework import serializers
from customers.models import BotUser, MessagesHistory


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'


class MessagesHistorySerializer(serializers.ModelSerializer):
    telegram_user_id = serializers.PrimaryKeyRelatedField(source='bot_user.telegram_user_id', read_only=True)

    class Meta:
        model = MessagesHistory
        fields = (
            'telegram_user_id',
            'text',
        )
