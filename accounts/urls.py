from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/editar/', UserUpdateView.as_view(), name='alterar_dados'),
]
