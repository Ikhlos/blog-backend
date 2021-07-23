from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from accounts import models

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(generic.UpdateView):
    model = models.CustomUser
    fields = ['phone', 'address', 'email']
    success_url = reverse_lazy('home')
    template_name = 'registration/detail.html'