from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog
from message.forms import MessageForm, ClientForm
from message.models import Message, Sending, Client


class MessageListView(ListView):
    model = Message

    def home(request):
        messages = Message.objects.all()
        blog_posts = Blog.objects.all()
        return render(request, 'message_list', {'messages': messages, 'blog_posts': blog_posts})

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    context_object_name = 'message'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    permission_required = 'message.add_message'
    success_url = reverse_lazy('message:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'message.change_message'
    success_url = reverse_lazy('message:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    # def has_permission(self) -> bool:
    #     perms = self.get_permission_required()
    #     if self.request.user.has_perms(perms):
    #         return True
    #
    #     message: Message = self.get_object()
    #     if self.request.user == message.owner:
    #         return True
    #
    #     return False

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('message:message_list')
    permission_required = 'message.delete_message'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

class ClientListView(ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    context_object_name = 'сlient'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object
class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'сlient.add_сlient'
    success_url = reverse_lazy('message:сlient_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'client.change_client'
    success_url = reverse_lazy('message:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('message:client_list')
    permission_required = 'client.delete_client'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

class SendingCreateView(CreateView):
    model = Sending
    fields = ('topic', 'client', 'period', 'send_at')

    def get_success_url(self):
        return reverse('message:sending_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['topic'] = get_object_or_404(Message, pk=self.kwargs.get('pk'))
        return context_data


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = Sending.PENDING
        obj.save()
        form.save_m2m()
        return super().form_valid(form)


class SendingListView(ListView):
    model = Sending

