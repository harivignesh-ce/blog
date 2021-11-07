from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("age",)
        fields = (
            "username",
            "email",
            "age",
        )
        help_texts = {
            "username": ("Enter a username"),
            "email": ("Enter your mail address"),
        }

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        email_added = cleaned_data.get("email")
        if not email_added:
            self.add_error("email", "Please enter your email address")
        if get_user_model().objects.filter(email=email_added).exists():
            self.add_error("email", "Email address already exists")
        return cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields
        fields = (
            "username",
            "email",
            "age",
        )
