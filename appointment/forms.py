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
        #fields = ( 'latitud', 'longitud','lugar', 'actividad','tipo_arbol','ciudad','nombre_comun','nombre_cientifico','familia','altura','dap','diametro_copa','comuna','barrio','recomendaciones','image')
        fields = ( 'latitud', 'longitud','codigo', 'version','numero_concepto', 'direccion','localidad','codigo_sigau','no_arbol','especie_vegetal','tipo_manejo','presencia_avifauna','manejo','observaciones','al_primer_fuste','al_segundo_fuste','al_tercer_fuste','al_cuarto_fuste','pe_primer_fuste','pe_segundo_fuste','pe_tercer_fuste','pe_cuarto_fuste','big_observaciones','fecha_medicion','fecha_trabajo','fecha_inicio','fecha_destoconado','fecha_recoleccion','valor_intervencion','image','image_2','image_3')

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        if self.instance:
            """ self.fields['actividad'].label = "Motivo"
            self.fields['lugar'].label = "Ubicacion"
            self.fields['ciudad'].label = "Ciudad"
            self.fields['tipo_arbol'].label = "Tipo de Arbol"
            self.fields['nombre_comun'].label = "Nombre Comun"
            self.fields['nombre_cientifico'].label = "Nombre Cientifico"
            self.fields['familia'].label = "Familia"
            self.fields['altura'].label = "Altura"
            self.fields['dap'].label = "Dap"
            self.fields['diametro_copa'].label = "Diametro Copa"
            self.fields['comuna'].label = "Comuna"
            self.fields['barrio'].label = "Barrio"
            self.fields['recomendaciones'].label = "Recomendaciones"
            self.fields['image'].label = "Imagen"
            self.fields['latitud'].label = "Latitud"
            self.fields['longitud'].label = "Longitud" """

            self.fields['latitud'].label = "Latitud"
            self.fields['longitud'].label = "Longitud"
            self.fields['codigo'].label = "Codigo"
            self.fields['version'].label = "Version"
            self.fields['numero_concepto'].label = "Numero Concepto"
            self.fields['direccion'].label = "Direccion"
            self.fields['localidad'].label = "Localidad"
            self.fields['codigo_sigau'].label = "Codigo Sigau"
            self.fields['no_arbol'].label = " Numero Arbol"
            self.fields['especie_vegetal'].label = "Especie Vegetal"
            self.fields['tipo_manejo'].label = "Tipo Manejo"
            self.fields['presencia_avifauna'].label = "Presencia de Avifauna"
            self.fields['manejo'].label = "Manejo"
            self.fields['observaciones'].label = "Observaciones"
            self.fields['al_primer_fuste'].label = "Altura Primer Fuste" 
            self.fields['al_segundo_fuste'].label = "Altura Segundo Fuste"
            self.fields['al_tercer_fuste'].label = "Altura Tercer Fuste"
            self.fields['al_cuarto_fuste'].label = "Altura Cuarto Fuste"
            self.fields['pe_primer_fuste'].label = "Perimetro Primer Fuste"
            self.fields['pe_segundo_fuste'].label = "Perimetro Segundo Fuste"
            self.fields['pe_tercer_fuste'].label = "Perimetro Tercer Fuste"
            self.fields['pe_cuarto_fuste'].label = "Perimetro Cuarto Fuste"
            self.fields['big_observaciones'].label = "Observaciones"
            self.fields['fecha_medicion'].label = "Fecha Medicion"
            self.fields['fecha_trabajo'].label = "Fecha Trabajo"
            self.fields['fecha_inicio'].label = "Fecha Inicio"
            self.fields['fecha_destoconado'].label = "Fecha Destoconado"
            self.fields['fecha_recoleccion'].label = "Fecha Recoleccion"
            self.fields['valor_intervencion'].label = "Valor Intervencion"
            self.fields['image'].label = "Imagen Antes"
            self.fields['image_2'].label = "Imagen Durante"
            self.fields['image_3'].label = "Imagen Despues"