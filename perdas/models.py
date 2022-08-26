from django.db import models


class ComunicacaoDePerda(models.Model):
    TIPOS_EVENTOS = [
        ('1', 'CHUVA EXCESSIVA'),
        ('2', 'GEADA'),
        ('3', 'GRANIZO'),
        ('4', 'SECA'),
        ('5', 'VENDAVAL'),
        ('6', 'RAIO'),
    ]

    nome_produtor = models.CharField(max_length=100, null=True)
    email_produtor = models.CharField(max_length=100, null=True)
    cpf_produtor = models.CharField(max_length=11, null=True)
    lat_lavoura = models.DecimalField(max_digits=22, decimal_places=16,
                                      null=True)
    lon_lavoura = models.DecimalField(max_digits=22, decimal_places=16,
                                      null=True)
    tipo_lavoura = models.CharField(max_length=50, null=True)
    data_colheita = models.DateField()
    evento = models.CharField(max_length=1, choices=TIPOS_EVENTOS,
                                    null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comunicação de perda'
        verbose_name_plural = 'Comunicações de perda'
        ordering = ['-atualizado_em']

    def __str__(self):
        return self.nome_produtor
