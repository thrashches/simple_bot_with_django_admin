from django.db import models


class BotUser(models.Model):
    telegram_user_id = models.IntegerField(unique=True, verbose_name='Id пользователя telegram')
    user_first_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.telegram_user_id)


class MessagesHistory(models.Model):
    bot_user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.bot_user.telegram_user_id}: {self.text[:100]}'
