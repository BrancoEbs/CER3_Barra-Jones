from django import forms
from .models import RegistroProduccion

class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'litros', 'fecha_produccion', 'turno']

    def clean_litros(self):
        litros = self.cleaned_data.get('litros')
        if litros <= 0:
            raise forms.ValidationError('La cantidad de litros debe ser positiva.')
        return litros
