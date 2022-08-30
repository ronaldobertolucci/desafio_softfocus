from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .models import ComunicacaoDePerda
from .views import *
from django.test import Client

class ComunicacaoDePerdaTests(TestCase):

    def setUp(self):

        self.analista = get_user_model().objects.create_user(
            username='user',
            email='user@email.com',
            first_name='Nome',
            last_name='Sobrenome',
            password='testpass123'
        )
        self.comunicacao = ComunicacaoDePerda.objects.create(
            analista=self.analista,
            nome_produtor='Produtor Teste',
            email_produtor='teste@teste.com',
            cpf_produtor='10090080099',
            lat_lavoura=52.445,
            lon_lavoura=78.44544,
            tipo_lavoura='milho',
            data_colheita='2022-02-15',
            evento='1',
        )

        self.analista_logado = Client()
        self.analista_logado.login(email='user@email.com',
                                   password='testpass123')

    # page view tests
    def test_comunicacao_create_view(self):
        view = resolve(f'/perdas/nova/')
        url = reverse('nova_comunicacao')
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/NoVa/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Nova comunicação de perda')
        self.assertTemplateUsed(
            user_response, 'perdas/nova-comunicacao.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ComunicacaoDePerdaCreateView.as_view().__name__
        )

    def test_comunicacao_detail_view(self):
        view = resolve(f'/perdas/{self.comunicacao.id}/')
        url = reverse('comunicacao', args=[self.comunicacao.id])
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/123456/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Detalhes da comunicação')
        self.assertTemplateUsed(
            user_response, 'perdas/comunicacao.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ComunicacaoDePerdaDetailView.as_view().__name__
        )

    def test_comunicacao_update_view(self):
        view = resolve(f'/perdas/{self.comunicacao.id}/editar/')
        url = reverse('editar_comunicacao', args=[self.comunicacao.id])
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/123456/editar/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Editar comunicação de perda')
        self.assertTemplateUsed(
            user_response, 'perdas/editar-comunicacao.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ComunicacaoDePerdaUpdateView.as_view().__name__
        )

    def test_comunicacao_delete_view(self):
        view = resolve(f'/perdas/{self.comunicacao.id}/excluir/')
        url = reverse('excluir_comunicacao', args=[self.comunicacao.id])
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/123456/excluir/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Excluir comunicação de perda')
        self.assertTemplateUsed(
            user_response, 'perdas/excluir-comunicacao.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ComunicacaoDePerdaDeleteView.as_view().__name__
        )

    def test_comunicacao_list_view(self):
        view = resolve(f'/perdas/')
        url = reverse('comunicacoes')
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/pErdAs/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Todas as comunicações')
        self.assertTemplateUsed(
            user_response, 'perdas/comunicacoes.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ComunicacaoDePerdaListView.as_view().__name__
        )

    def test_pesquise_cpf_view(self):
        view = resolve(f'/perdas/cpf/')
        url = reverse('pesquise_cpf')
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/CPF/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Resultados')
        self.assertTemplateUsed(
            user_response, 'perdas/pesquise-cpf.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            PesquiseCPFListView.as_view().__name__
        )

    def test_pesquise_cpf_view(self):
        view = resolve(f'/perdas/exportar/')
        url = reverse('exportar')
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/perdas/ExPorTar/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Exportar')
        self.assertTemplateUsed(
            user_response, 'perdas/exportar.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            ExportarComunicacaoDePerdaView.as_view().__name__
        )

    # model tests
    def test_comunicacao_analista_content(self):
        analista_objeto = self.comunicacao.analista
        self.assertEqual(analista_objeto, self.analista)

    def test_comunicacao_nome_produtor_content(self):
        nome_produtor_objeto = self.comunicacao.nome_produtor
        self.assertEqual(nome_produtor_objeto, 'Produtor Teste')

    def test_comunicacao_email_produtor_content(self):
        email_produtor_objeto = self.comunicacao.email_produtor
        self.assertEqual(email_produtor_objeto, 'teste@teste.com')

    def test_comunicacao_cpf_produtor_content(self):
        cpf_produtor_objeto = self.comunicacao.cpf_produtor
        self.assertEqual(cpf_produtor_objeto, '10090080099')

    def test_comunicacao_lat_lavoura_content(self):
        lat_lavoura_objeto = self.comunicacao.lat_lavoura
        self.assertEqual(lat_lavoura_objeto, 52.445)

    def test_comunicacao_lon_lavoura_content(self):
        lon_lavoura_objeto = self.comunicacao.lon_lavoura
        self.assertEqual(lon_lavoura_objeto, 78.44544)

    def test_comunicacao_tipo_lavoura_content(self):
        tipo_lavoura_objeto = self.comunicacao.tipo_lavoura
        self.assertEqual(tipo_lavoura_objeto, 'milho')

    def test_comunicacao_data_colheita_content(self):
        data_colheita_objeto = self.comunicacao.data_colheita
        self.assertEqual(data_colheita_objeto, '2022-02-15')

    def test_comunicacao_evento_content(self):
        evento_objeto = self.comunicacao.evento
        self.assertEqual(evento_objeto, '1')

    def test_comunicacao_string_representation(self):
        self.assertEqual(str(self.comunicacao), self.comunicacao.nome_produtor)
