"""User forms."""

from django import forms
from abjhelp.users.models import HelpRequest, DonorRequest


class HelpRequestForm(forms.Form):

    name = forms.CharField(
        min_length=2,
        max_length=50,
        label='Nombre',
        error_messages={
            'required': 'Este campo es requerido',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    description = forms.CharField(
        label='Descripción del pedido',
        required=False,
        error_messages={
            'required': 'Este campo es requerido',
        },
        widget=forms.Textarea(
            attrs={
                "rows": 5, "cols": 20,
                'class': 'form-control',
            }),
    )
    phone_number = forms.CharField(
        label='Número del celular de contacto',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
        error_messages={
            'required': 'Este campo es requerido',
        },
    )

    address = forms.CharField(
        min_length=2,
        max_length=50,
        label='¿Dónde estás ubicado?',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )

    def save(self):
        """Create help resquest."""
        data = self.cleaned_data
        help_request = HelpRequest.objects.get_or_create(**data)
        return help_request


class DonorRequestForm(forms.Form):

    name = forms.CharField(
        min_length=2,
        max_length=50,
        label='¿Cuál es tu nombre?',
        error_messages={
            'required': 'Este campo es requerido',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )

    phone_number = forms.CharField(
        label='Número de whatsapp',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
        error_messages={
            'required': 'Este campo es requerido',
        },
    )
    email = forms.EmailField(
        min_length=2,
        max_length=50,
        required=False,
        label='¿Cuál es tu correo?',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        error_messages={
            'invalid': 'Porfavor ingrese un correo válido',
        },
    )
    address = forms.CharField(
        label='¿Dónde estás ubicado?',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
    )

    def save(self):
        """Create Donor resquest."""
        data = self.cleaned_data
        donor_request = DonorRequest.objects.get_or_create(**data)
        return donor_request
