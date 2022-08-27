from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "account/update.html"
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id
