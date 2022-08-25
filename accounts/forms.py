from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label='Primeiro nome',
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    last_name = forms.CharField(
        max_length=30,
        label='Último nome',
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'})
    )

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


# form para editar o usuário
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )
        widgets = {
            'email': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
            }),
        }
