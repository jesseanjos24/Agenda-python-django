from typing import Any
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from contact.models import Contact
from django import forms
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
    ...