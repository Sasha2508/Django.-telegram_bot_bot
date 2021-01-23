# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import requests
import telebot
from bot.models import Subscriber, Message
import datetime


class Command(BaseCommand):
    help = 'Test'
    def handle(self, *args, **options):
        bot_id = '1562943656:AAGVqGH7LMn6JrDsPIvvAUhDHJt7RweCo_A'
        bot = telebot.TeleBot(bot_id)
        messages = Message.objects.filter(is_sent=False)
        subscribers = Subscriber.objects.all()
        for message in messages:
            for subscriber in subscribers:
                bot.send_message(subscriber.telegram_id, message.message_text)
            message.is_sent=True
            message.sending_time=datetime.datetime.utcnow()
            message.save()
