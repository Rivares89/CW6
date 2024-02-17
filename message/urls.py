from django.urls import path, include

from message.apps import MessageConfig
from message.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    SendingCreateView, SendingListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('', include('blog.urls', namespace='blog')),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('create/', MessageCreateView.as_view(), name='create_message'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('sending_create/<int:pk>/', SendingCreateView.as_view(), name='create_sending'),
    path('list/', SendingListView.as_view(), name='sending_list')
]