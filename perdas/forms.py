from django import forms
from .models import ComunicacaoDePerda


class ComunicacaoDePerdaForm(forms.ModelForm):
    class Meta:
        model = ComunicacaoDePerda
        fields = ("nome_produtor", "email_produtor", "cpf_produtor",
                  "lat_lavoura", "lon_lavoura", "tipo_lavoura", "data_colheita",
                  "evento")
        widgets = {
            'lat_lavoura': forms.NumberInput(attrs={
                'placeholder': "Ex.: -22,194"}
            ),
            'lon_lavoura': forms.NumberInput(attrs={
                'placeholder': "Ex.: -46,757"}
            ),
        }
        labels = {
            "nome_produtor": "Nome completo",
            "email_produtor": "email",
            "cpf_produtor": "CPF (somente números)",
            "lat_lavoura": "Latitude",
            "lon_lavoura": "Longitude",
            "tipo_lavoura": "Tipo da lavoura",
            "data_colheita": "Data da colheita",
        }


class ExportarDadosForm(forms.Form):
    TIPOS_DE_SAIDA =(
        ("csv", ".csv"),
        ("xlsx", ".xlsx"),
        ("json", ".json"),
    )
    tipo = forms.ChoiceField(choices = TIPOS_DE_SAIDA)
