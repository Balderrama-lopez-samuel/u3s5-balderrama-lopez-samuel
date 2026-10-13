# forms: herramientas de Django para construir y validar formularios
from django import forms
from .models import Servicio

# ServicioForm: un ModelForm arma los campos del formulario a partir del modelo Servicio
class ServicioForm(forms.ModelForm):
    # Meta: le dice al ModelForm de qué modelo sale y qué campos mostrar
    class Meta:
        model = Servicio
        # propietario queda fuera a propósito: lo asigna la vista con request.user
        fields = ['titulo', 'descripcion', 'precio', 'categoria']

    # clean_precio: validación personalizada, Django la llama solo al ejecutar is_valid()
    def clean_precio(self):
        # cleaned_data: los datos ya convertidos a su tipo (precio llega como Decimal)
        precio = self.cleaned_data['precio']
        if precio <= 0:
            # ValidationError: el mensaje aparece en pantalla junto al campo precio
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return precio
