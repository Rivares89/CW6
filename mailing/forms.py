from django import forms
from django.forms.widgets import DateTimeInput
from .models import Mailing

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('topic', 'recipients', 'send_at')
        widgets = {
            'send_at': DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }