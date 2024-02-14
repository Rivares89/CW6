from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView

from mailing.models import Mailing
from mailing.services import send_letter
from message.models import Message


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('topic', 'recipients', 'send_at')

    def get_success_url(self):
        return reverse('mailing:mailing_list')

    # args = [self.kwargs.get('pk')]
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['topic'] = get_object_or_404(Message, pk=self.kwargs.get('pk'))
        # context_data['recipients'] = get_object_or_404(Client, pk=self.kwargs.get('pk'))
        return context_data


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = Mailing.PENDING
        obj.save()
        form.save_m2m()  # не забудьте сохранить связи many-to-many
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing