from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('create/<int:pk>/', MailingCreateView.as_view(), name='create')
]