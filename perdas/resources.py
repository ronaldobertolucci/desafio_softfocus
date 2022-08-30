from import_export import resources
from .models import ComunicacaoDePerda


class ComunicacaoDePerdaResource(resources.ModelResource):
    class Meta:
        model = ComunicacaoDePerda
