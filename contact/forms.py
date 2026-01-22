from typing import Any
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import Contact
from django import forms
from django.contrib.auth import password_validation
import os

def validar_nome_imagem(value):
        nome_arquivo = os.path.basename(value.name)

        LIMITE = 150  # você define

        if len(nome_arquivo) > LIMITE:
            raise ValidationError(
                'O nome da imagem é muito grande. Por favor, renomeie o arquivo.'
            )


class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        required=False,
        validators=[validar_nome_imagem],
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
       
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone','category', 'description', 'picture']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number - (XX) XXXXX-XXXX'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
        
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
        
#    def clean(self) -> dict[str, Any]:
#        cleaned_data = self.cleaned_data
#        self.add_error(
#            'first_name',
#            ValidationError('Custom error message for first name field.', code='invalid')
#        )
#        
#        return super().clean()
    
    def clean_first_name(self) -> str:
        first_name = self.cleaned_data.get('first_name', '')
        
        if 'invalid' in first_name.lower():
            raise ValidationError('First name cannot contain the word "invalid".', code='invalid')
        
        return first_name
    
    def clean_phone(self) -> str:
        phone = self.cleaned_data.get('phone', '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '').strip()
        
        if not phone.isdigit():
            raise ValidationError('Phone number must contain only digits.', code='invalid')
        
        if len(phone) < 10:
            raise ValidationError('Phone number must be at least 11 digits long.', code='invalid')
        
        return phone

      
class ResgisterForm(UserCreationForm):
    
    first_name = forms.CharField(
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control',})
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control',})
    )
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Este nome de usuário já está em uso.'
            )

        return username
    
    def clean_email(self) -> str:
        email = self.cleaned_data.get('email', '')
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already in use.', code='invalid')
        
        return email


class RegisteUpdateForm(forms.ModelForm):
     
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1