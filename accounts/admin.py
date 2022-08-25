from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    ordering = ('email',)
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_staff',
    ]

    # Caso seja necessário adicionar mais campos na PÁGINA admin

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('telefone',)}),
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('telefone',)}),

admin.site.register(CustomUser, CustomUserAdmin)
