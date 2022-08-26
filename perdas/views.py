from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComunicacaoDePerda
from .forms import ComunicacaoDePerdaForm
from django.urls import reverse_lazy


class ComunicacaoDePerdaCreateView(LoginRequiredMixin, CreateView):
    form_class = ComunicacaoDePerdaForm
    model = ComunicacaoDePerda
    template_name = 'perdas/nova-comunicacao.html'
    success_url = reverse_lazy('home')


class ComunicacaoDePerdaDetailView(LoginRequiredMixin, DetailView):
    model = ComunicacaoDePerda
    template_name = 'perdas/comunicacao.html'


class ComunicacaoDePerdaUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ComunicacaoDePerdaForm
    model = ComunicacaoDePerda
    template_name = 'perdas/editar-comunicacao.html'
    success_url = reverse_lazy('home')


class ComunicacaoDePerdaDeleteView(LoginRequiredMixin, DeleteView):
    model = ComunicacaoDePerda
    template_name = "perdas/excluir-comunicacao.html"
    success_url = reverse_lazy('home')