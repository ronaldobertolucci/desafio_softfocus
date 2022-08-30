from django.urls import path
from .views import *

urlpatterns = [
    path(
        'nova/',
        ComunicacaoDePerdaCreateView.as_view(),
        name='nova_comunicacao'
    ),
    path(
        '<int:pk>/',
        ComunicacaoDePerdaDetailView.as_view(),
        name='comunicacao'
    ),
    path(
        '<int:pk>/editar/',
        ComunicacaoDePerdaUpdateView.as_view(),
        name='editar_comunicacao'
    ),
    path(
        '<int:pk>/excluir/',
        ComunicacaoDePerdaDeleteView.as_view(),
        name='excluir_comunicacao'
    ),
    path(
        '',
        ComunicacaoDePerdaListView.as_view(),
        name='comunicacoes'
    ),
    path('cpf/', PesquiseCPFListView.as_view(), name='pesquise_cpf'),
    path('dados', ComunicacaoDePerdaDataView.as_view(), name='dados'),
]
