# Generated by Django 4.1.7 on 2023-02-16 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_user_id', models.IntegerField(verbose_name='Id пользователя telegram')),
                ('user_first_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessagesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('bot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.botuser')),
            ],
        ),
    ]
