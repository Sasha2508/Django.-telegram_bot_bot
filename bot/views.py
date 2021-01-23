from django.http.response import JsonResponse, HttpResponse
import json
import datetime

from rest_framework import generics
from .models import Subscriber, Message
from .serializers import SubscriberListSerializer, MessageListSerializer


class SubscribersList(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberListSerializer

class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageListSerializer

class MessageRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        data = list(messages.values('id', 'message_text'))
    else:
        data = {'status': False, 'error': 'Method is not supported'}
    return JsonResponse(data, safe=False)


def message_add(request):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            new_message = Message.objects.create(
                is_sent=request_json['send'],
                message_text=request_json['text_message']
            )
            json_response['status'] = True
            status_code = 201
            json_response['result'] = {
                'message_id': new_message.id,
                'text_message': new_message.message_text,
                'is_send': new_message.is_sent
            }
        except BaseException:
            json_response['error_message'] = 'Bad request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)


def get_message(request, message_id):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'GET':
        try:
            message = Message.objects.get(id=message_id)

            json_response['result'] = {
                'message_id': message.id,
                'text_message': message.message_text,
                'is_send': message.is_sent
            }
            json_response['status'] = True
            status_code = 201
        except BaseException:
            json_response['error_message'] = 'Bad request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)

def update_message(request, message_id):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method in ['PUT', 'PATCH']:
        try:
            request_json = json.loads(request.body)
            message = Message.objects.get(id=message_id)
            message.message_text = request_json['message_text']
            message.is_sent = request_json['is_sent']
            message.save()
            json_response['result'] = {
                'message_id': message.id,
                'text_message': message.message_text,
                'is_send': message.is_sent
            }
            json_response['status'] = True
            status_code = 201
        except BaseException:
            json_response['error_message'] = 'Bad request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)


def delete_message(request, message_id):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'DELETE':
        try:
            message = Message.objects.get(id=message_id)
            message.delete()
            json_response['status'] = True
            status_code = 200
        except BaseException:
            json_response['error_message'] = 'Bad Request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)