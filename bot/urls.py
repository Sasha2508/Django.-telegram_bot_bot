from django.urls import path
from .views import SubscribersList, MessageList, MessageCreate, MessageRUD, message_list, message_add, get_message, update_message, delete_message

urlpatterns = [
    path('subscribers/list/', SubscribersList.as_view()),
    path('messages/list/', MessageList.as_view()),
    path('messages/add/', MessageCreate.as_view()),
    path('messages/<int:pk>/', MessageRUD.as_view()),
    path('messages/custom_list/', message_list),
    path('messages/custom/add/', message_add),
    path('messages/custom/get/<int:message_id>/', get_message),
    path('messages/custom/update/<int:message_id>/', update_message),
    path('messages/custom/delete/<int:message_id>/', delete_message)
]