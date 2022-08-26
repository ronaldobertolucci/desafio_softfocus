from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth import get_user_model
from .views import *
from django.test import Client

class HomepageTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class DashboardTests(TestCase):

    def setUp(self):

        self.analista = get_user_model().objects.create_user(
            username='user',
            email='user@email.com',
            first_name='Nome',
            last_name='Sobrenome',
            password='testpass123'
        )

        self.analista_logado = Client()
        self.analista_logado.login(email='user@email.com',
                                   password='testpass123')

    def test_dashboard_view(self):
        view = resolve(f'/dashboard/')
        url = reverse('dashboard')
        response = self.client.get(url)
        no_response = self.analista_logado.get(f'/DasHboarD/')
        user_response = self.analista_logado.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Dashboard')
        self.assertTemplateUsed(
            user_response, 'pages/dashboard.html'
        )
        self.assertNotContains(
            user_response, 'Ei! Não estou na página.'
        )
        self.assertEqual(
            view.func.__name__,
            DashboardView.as_view().__name__
        )
