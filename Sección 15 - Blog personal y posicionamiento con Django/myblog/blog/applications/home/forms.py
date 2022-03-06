from django import forms

# models
from .models import Suscribers

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico', 
                  # 'class': 'input-email'
                }
            )
        }