from django.contrib import admin
from .models import ComunicacaoDePerda

class ComunicacaoDePerdaAdmin(admin.ModelAdmin):
    list_display = ("nome_produtor", "tipo_lavoura", "data_colheita",
                    "evento")

admin.site.register(ComunicacaoDePerda, ComunicacaoDePerdaAdmin)
