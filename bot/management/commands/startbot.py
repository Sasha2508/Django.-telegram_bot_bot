# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import requests
import telebot
from bot.models import Subscriber


class Command(BaseCommand):
    help = 'Test'
    def handle(self, *args, **options):
        bot_id = '1562943656:AAGVqGH7LMn6JrDsPIvvAUhDHJt7RweCo_A'
        self.bot_starter(bot_id)



    def start_bot(self, bot_id):
        print(f'startbot')
        bot = telebot.TeleBot(bot_id)
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            subscriber = Subscriber.objects.filter(telegram_id=int(message.chat.id))
            if len(subscriber) > 0:
                bot.send_message(message.chat.id, 'Welcome Back, ' + message.from_user.first_name)
            else:
                Subscriber.objects.create(
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                    user_name=message.from_user.username,
                    telegram_id=message.chat.id

                )
                bot.send_message(message.chat.id, 'Welcome to the chat, ' + message.from_user.first_name)

        bot.polling(timeout=1)


    def bot_starter(self, bot_id):
        try:
            self.start_bot(bot_id)
        except BaseException:
            print(f'Exception worked')
            self.bot_starter(bot_id)



#HTTP API:1562943656:AAGVqGH7LMn6JrDsPIvvAUhDHJt7RweCo_A
#https://api.telegram.org/bot1562943656:AAGVqGH7LMn6JrDsPIvvAUhDHJt7RweCo_A/getUpdates
#https://api.telegram.org/botID:HASH/sendMessage
#id : 1345170602

# chat_id = '1345170602'
        # message = 'Hello, World!'
        # base_url = 'https://api.telegram.org/bot'+bot_id+'/sendMessage?chat_id='+chat_id+'&text='+message
        # requests.get(base_url)
        # print(f'Message sent')

