from typing import Any
from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone',]
        
    def clean(self) -> dict[str, Any]:
        #cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError('Custom error message for first name field.', code='invalid')
        )
        
        return super().clean()
    
