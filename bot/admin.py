from django.contrib import admin
from .models import *

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'user_name',
        'telegram_id'
    ]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sending_time',
        'is_sent',
        'message_text'
    ]
