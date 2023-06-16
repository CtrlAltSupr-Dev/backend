from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(f"-> Email: {email}")
        if email and not email.endswith('@gmail.com'):
            raise ValidationError("El correo debe ser de extensión @uc.cl")
        return email

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
