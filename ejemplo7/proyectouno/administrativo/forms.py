from django.forms import ModelForm
from django import forms

from administrativo.models import Matricula, Modulo, Estudiante

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']



class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()
        self.initial['costo'] = self.instance.costo
        self.fields["costo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {'comentario': forms.Textarea(attrs={'rows': 4,'cols': 40,'placeholder': 'Escribe aquí tu comentario...'}),}


class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if Modulo.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un módulo con ese nombre. Ingrese uno diferente.")
        return nombre

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        if len(valor.split()) < 2:
            raise forms.ValidationError("Ingrese al menos dos nombres.")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        if len(valor.split()) < 2:
            raise forms.ValidationError("Ingrese al menos dos apellidos.")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if not valor.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números.")
        if len(valor) != 10:
            raise forms.ValidationError("La cédula debe tener exactamente 10 dígitos.")
        return valor

    def clean_edad(self):
        valor = self.cleaned_data['edad']
        if not isinstance(valor, int):
            raise forms.ValidationError("La edad debe ser un número.")
        if valor <= 0:
            raise forms.ValidationError("La edad debe ser mayor a 0.")
        return valor