from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView

app_name = MailingConfig.name

urlpatterns = [
    path('create/<int:pk>/', MailingCreateView.as_view(), name='create'),
    path('list/', MailingListView.as_view(), name='mailing_list')
]