from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    to_be_added = ((None, {"fields": ("age",)}),)
    fieldsets = UserAdmin.fieldsets + to_be_added
    add_fieldsets = UserAdmin.add_fieldsets + to_be_added


admin.site.register(CustomUser, CustomUserAdmin)
