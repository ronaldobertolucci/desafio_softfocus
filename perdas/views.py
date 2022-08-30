from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import ComunicacaoDePerda
from .forms import ComunicacaoDePerdaForm, ExportarDadosForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from .resources import ComunicacaoDePerdaResource


class PesquiseCPFListView(LoginRequiredMixin, ListView):
    model = ComunicacaoDePerda
    context_object_name = 'comunicacoes'
    template_name = 'perdas/pesquise-cpf.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return ComunicacaoDePerda.objects.filter(
            Q(cpf_produtor__iexact=query) | Q(cpf_produtor__exact=query)
        )


class ComunicacaoDePerdaCreateView(LoginRequiredMixin, CreateView):
    form_class = ComunicacaoDePerdaForm
    model = ComunicacaoDePerda
    template_name = 'perdas/nova-comunicacao.html'
    success_url = reverse_lazy('comunicacoes')

    def form_valid(self, form):
        form.instance.analista = self.request.user
        return super().form_valid(form)


class ComunicacaoDePerdaDetailView(LoginRequiredMixin, DetailView):
    model = ComunicacaoDePerda
    template_name = 'perdas/comunicacao.html'


class ComunicacaoDePerdaUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ComunicacaoDePerdaForm
    model = ComunicacaoDePerda
    template_name = 'perdas/editar-comunicacao.html'
    success_url = reverse_lazy('comunicacoes')


class ComunicacaoDePerdaDeleteView(LoginRequiredMixin, DeleteView):
    model = ComunicacaoDePerda
    template_name = "perdas/excluir-comunicacao.html"
    success_url = reverse_lazy('comunicacoes')


class ComunicacaoDePerdaListView(LoginRequiredMixin, ListView):
    model = ComunicacaoDePerda
    template_name = 'perdas/comunicacoes.html'
    context_object_name = 'comunicacoes'
    paginate_by = 8


class ComunicacaoDePerdaDataView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        perdas = ComunicacaoDePerda.objects.all()
        data = perdas.values()
        return JsonResponse(list(data), safe=False)


class ExportarComunicacaoDePerdaView(LoginRequiredMixin, View):
    context = {}

    def get(self, request, *args, **kwargs):
        form = ExportarDadosForm()
        self.context['form'] = form
        if request.GET:
            tipo = request.GET['tipo']
            return self.export(tipo)
        return render(request,'perdas/exportar.html', self.context)

    def export(self, tipo):
        perdas_resource = ComunicacaoDePerdaResource()
        dataset = perdas_resource.export()
        if tipo == 'csv':
            response = HttpResponse(dataset.csv, content_type=f'text/csv')
        elif tipo == 'json':
            response = HttpResponse(dataset.json,
                                    content_type='application/json')
        elif tipo == 'xlsx':
            response = HttpResponse(dataset.xlsx,
                                    content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;'
        response['Content-Disposition'] += f'filename="perdas.{tipo}"'
        return response
