from rest_framework import serializers
from .models import Subscriber, Message

class SubscriberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'sending_time',
            'is_sent',
            'message_text'
        ]
        #fields = '__all__'

