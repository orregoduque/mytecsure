from django.contrib.auth import get_user_model
from django import forms
from .models import *

class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = '__all__'


class directorProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = '__all__'

    """ 
    cedula_acudiente 
    cumpleanos_acudiente 
    email_acudiente 
    direccion_acudiente 
    barrio_acudiente 
    comuna_acudiente 
    trabajo_acudiente 
    celular_acudiente 
    id_seguro 
    identidad_seguro 
    descripcion_seguro
    condicion_especial
    descripcion_condicion_especial
    """