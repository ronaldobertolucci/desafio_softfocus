from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from django.test import Client
from .views import UserUpdateView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user',
            email='user@email.com',
            first_name='Nome',
            last_name='Sobrenome',
            password='testpass123'
        )
        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'user@email.com')
        self.assertEqual(user.first_name, 'Nome')
        self.assertEqual(user.last_name, 'Sobrenome')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            first_name='Nome',
            last_name='Sobrenome',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertEqual(admin_user.first_name, 'Nome')
        self.assertEqual(admin_user.last_name, 'Sobrenome')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class UpdatePageViewTest(TestCase):

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username='user',
            email='user@email.com',
            first_name='Nome',
            last_name='Sobrenome',
            password='testpass123'
        )
        outro_usuario = get_user_model().objects.create_user(
            username='user2',
            email='user2@email.com',
            first_name='Nome2',
            last_name='Sobrenome2',
            password='testpass123'
        )

        self.usuario_logado = Client()
        self.usuario_logado.login(email='user@email.com',
                                  password='testpass123')
        self.outro_usuario_logado = Client()
        self.outro_usuario_logado.login(email='user2@email.com',
                                        password='testpass123')

    def test_update_view(self):
        view = resolve(f'/accounts/{self.usuario.pk}/editar/')
        user_response = self.usuario_logado.get(reverse(
            'alterar_dados',
            args=[self.usuario.pk]
        ))
        another_user_response = self.outro_usuario_logado.get(
            reverse('alterar_dados', args=[self.usuario.pk])
        )
        self.assertEqual(another_user_response.status_code, 403)
        self.assertEqual(user_response.status_code, 200)
        self.assertContains(user_response, 'Altere seus dados')
        self.assertTemplateUsed(user_response, 'account/update.html')
        self.assertEqual(
            view.func.__name__,
            UserUpdateView.as_view().__name__
        )
