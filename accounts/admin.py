"""
Admin for accounts app.
Dec 19, 2021
@narender

"""
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin Class.
    """
    add_form = UserCreationForm
    form = UserChangeForm 
    model = CustomUser 

    list_display = ('roll','email','name','is_staff','is_active',)
    list_filter = ('roll','email','name','is_staff','is_active',)

    fieldsets = (
        (None, {'fields': ('roll', 'email','name', 'password')}) ,
        ('Permissions', {'fields':('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('roll','email','name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('roll',)
    ordering = ('roll',)


admin.site.register(CustomUser,CustomUserAdmin)
