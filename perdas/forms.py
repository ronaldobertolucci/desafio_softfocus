from django import forms
from .models import ComunicacaoDePerda


class ComunicacaoDePerdaForm(forms.ModelForm):
    class Meta:
        model = ComunicacaoDePerda
        fields = ("nome_produtor", "email_produtor", "cpf_produtor",
                  "lat_lavoura", "lon_lavoura", "tipo_lavoura", "data_colheita",
                  "evento")
        labels = {
            "nome_produtor": "Nome",
            "email_produtor": "email",
            "cpf_produtor": "CPF",
            "lat_lavoura": "Latitude",
            "lon_lavoura": "Longitude",
            "tipo_lavoura": "Tipo da lavoura",
            "data_colheita": "Data da colheita",
        }