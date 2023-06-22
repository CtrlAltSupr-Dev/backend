from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if not (email.endswith('@uc.cl') or email.endswith('@ing.puc.cl')):
                raise ValidationError("El correo debe ser de extensión válida.")
        return email

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
