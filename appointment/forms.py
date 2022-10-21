from django import forms
from .models import *
from django.contrib.auth import get_user_model
from user_profile.models import UserProfile
User = get_user_model()


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('student', 'sintomas', 'estado')

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['student'].queryset = User.objects.filter(user_type="S")
            self.fields['sintomas'].label = "Motivo"
            self.fields['estado'].label = "Estado actividad"

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        #fields = '__all__'
        fields = ('actividad',)

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        if self.instance:
            #self.fields["date"].label = "Date (YYYY-MM-DD)"
            self.fields['actividad'].label = "Motivo"

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        #fields = '__all__'
        fields = ('student', 'lugar', 'actividad','tipo_arbol',)

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        if self.instance:
            #self.fields["date"].label = "Date (YYYY-MM-DD)"
            self.fields['student'].queryset = User.objects.filter(user_type="S")
            self.fields['actividad'].label = "Motivo"
            self.fields['lugar'].label = "Ubicacion"
            self.fields['tipo_arbol'].label = "Tipo de Arbol"