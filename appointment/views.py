from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext
from .models import * 
from .forms import * 
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import UserProfile
from account.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

import csv
import datetime


# Create your views here.
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


#############################################################################################
#ACTIVIDADES
class PrescriptionStudentView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10

    def get_queryset(self):
        estudiante = self.request.user.id
        return Prescription.objects.filter(student_id=estudiante).order_by('-date')

class PrescriptionListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10
    def get_queryset(self):
        prescription = Prescription.objects.all().order_by('-date')
        return Prescription.objects.all().order_by('-date')
        #return Prescription.objects.all().order_by('-date').exclude(utxt='admin')

@login_required(login_url='/login/')
def PrescriptionCreateView(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.director = request.user
            prescription.date = datetime.datetime.now()
            prescription.save()
            return redirect('appointment:doc-prescriptions')
    else:
        form = PrescriptionForm()
    return render(request, 'appointment/prescription_create.html', {'form': form})

#update prescription
@login_required(login_url='/login/')
def prescription_edit(request, id=None):
    instance = get_object_or_404(Prescription, id = id)
    form = PrescriptionForm(request.POST or None, instance = instance )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('appointment:doc-prescriptions')
    context = {
            "title" : 'Edit' + str(instance.estado),
            'instance': instance,
            'form': form,
    }
    return render(request, 'appointment/prescription_create.html', context)
#############################################################################################

#############################################################################################
@login_required(login_url='/login/')
def rdashboard(request):
    #if request.method == "GET" and request.user.user_type == "R":
    if request.method == "GET":
        context = {
            "totalApp" : len(Prescription.objects.all()),
            "compApp" : len(Prescription.objects.filter(status="Completed")),
            "pendApp" : len(Prescription.objects.filter(status="Pending")),
            "app_list" : Prescription.objects.all(),
            "pat_list" : UserProfile.objects.filter(user__user_type="P")[:5]
        }
        return render(request, 'appointment/r_dashboard.html', context=context)
#############################################################################################

#############################################################################################
@login_required(login_url='/login/')
def hrdashboard(request):
    #if request.method == "GET" and request.user.user_type == "HR":
    if request.method == "GET":
        context = {
            "totalPat" : len(User.objects.filter(user_type="P")),
            "totalDoc" : len(User.objects.filter(user_type="D")),
            "ondutyDoc" : len(UserProfile.objects.filter(status="Active").filter(user__user_type="D")),
            "doc_list" : UserProfile.objects.filter(user__user_type="D")
        }
        return render(request, 'appointment/hr_dashboard.html', context=context)
#############################################################################################

#############################################################################################
@login_required(login_url='/login/')
def hraccounting(request):
    #if request.method == "GET" and request.user.user_type == "HR":
    if request.method == "GET":
        context = {
            "payment_ind" : Prescription.objects.filter(payment_type="I"),
            "payment_cons" : Prescription.objects.filter(payment_type="C"),
        }
        return render(request, 'appointment/accounting.html', context=context)
#############################################################################################


#############################################################################################
#NOTAS
@login_required(login_url='/login/')
def NotaCreateView(request):
    
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.student = request.user
            nota.date = datetime.datetime.now()
            nota.save()
            return redirect('appointment:student-notas')
    else:
        form = NotaForm()
    return render(request, 'appointment/nota_create.html', {'form': form})


class NotasForAstudentView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10
    
    def get_queryset(self):
        estudiante = self.request.user.id
        return Nota.objects.filter(student_id=estudiante).order_by('date')

class NotasForAdirectorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10

    def get_queryset(self):
        return Nota.objects.all().order_by('date')
#############################################################################################


#############################################################################################
#EVENTOS

COORDENADAS = [ 
    ('Colombo', '3.337044-76.543025'),
    ('Americano', '3.378298-76.544850'),
    ('Frances', '3.486792-76.521890'),
    ('Bolivar', '3.340611-76.546607'),
    ('Finca', '3.220535-76.582756'),
    ('Teatro', '3.449569-76.535987'),
]


@login_required(login_url='/login/')
def EventoCreateView(request):
    
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data.get("codigo")
            version = form.cleaned_data.get("version")
            numero_concepto = form.cleaned_data.get("numero_concepto")
            direccion = form.cleaned_data.get("direccion")
            numero = form.cleaned_data.get("numero")
            localidad = form.cleaned_data.get("localidad")
            codigo_sigau = form.cleaned_data.get("codigo_sigau")
            no_arbol = form.cleaned_data.get("no_arbol")
            especie_vegetal = form.cleaned_data.get("especie_vegetal")
            tipo_manejo = form.cleaned_data.get("tipo_manejo")
            presencia_avifauna = form.cleaned_data.get("presencia_avifauna")
            manejo = form.cleaned_data.get("manejo")
            observaciones = form.cleaned_data.get("observaciones")
            al_primer_fuste = form.cleaned_data.get("al_primer_fuste")
            al_segundo_fuste = form.cleaned_data.get("al_segundo_fuste")
            al_tercer_fuste = form.cleaned_data.get("al_tercer_fuste")
            al_cuarto_fuste = form.cleaned_data.get("al_cuarto_fuste")
            pe_primer_fuste = form.cleaned_data.get("pe_primer_fuste")
            pe_segundo_fuste = form.cleaned_data.get("pe_segundo_fuste")
            pe_tercer_fuste = form.cleaned_data.get("pe_tercer_fuste")
            pe_cuarto_fuste = form.cleaned_data.get("pe_cuarto_fuste")
            big_observaciones = form.cleaned_data.get("big_observaciones")
            fecha_medicion = form.cleaned_data.get("fecha_medicion")
            fecha_trabajo = form.cleaned_data.get("fecha_trabajo")
            fecha_inicio = form.cleaned_data.get("fecha_inicio")
            fecha_destoconado = form.cleaned_data.get("fecha_destoconado")
            fecha_recoleccion = form.cleaned_data.get("fecha_recoleccion")
            valor_intervencion = form.cleaned_data.get("valor_intervencion")
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud")


            """ username = form.cleaned_data.get("student")
            destino = form.cleaned_data.get("lugar")
            arbol = form.cleaned_data.get("tipo_arbol")
            ciudad = form.cleaned_data.get("ciudad")
            numero = form.cleaned_data.get("numero")
            nombre_comun = form.cleaned_data.get("nombre_comun")
            nombre_cientifico = form.cleaned_data.get("nombre_cientifico")
            familia = form.cleaned_data.get("familia")
            altura = form.cleaned_data.get("altura")
            dap = form.cleaned_data.get("dap")
            diametro_copa = form.cleaned_data.get("diametro_copa")
            comuna = form.cleaned_data.get("comuna")
            barrio = form.cleaned_data.get("barrio")
            recomendaciones = form.cleaned_data.get("recomendaciones")
            latitud = form.cleaned_data.get("latitud")
            longitud = form.cleaned_data.get("longitud") """

            if len(request.FILES) != 0:
                imagen = request.FILES["image"]
                imagen_2 = request.FILES["image_2"]
                imagen_3 = request.FILES["image_3"]
        
            evento = form.save(commit=False)
            evento.student = request.user
            evento.codigo = codigo
            evento.date = datetime.datetime.now()
            evento.version = version
            evento.numero_concepto = numero_concepto
            evento.direccion = direccion
            evento.localidad = localidad
            evento.codigo_sigau = codigo_sigau
            evento.no_arbol = no_arbol
            evento.especie_vegetal = especie_vegetal
            evento.tipo_manejo = tipo_manejo
            evento.presencia_avifauna = presencia_avifauna
            evento.manejo = manejo
            evento.observaciones = observaciones
            evento.al_primer_fuste = al_primer_fuste
            evento.al_segundo_fuste = al_segundo_fuste
            evento.al_tercer_fuste = al_tercer_fuste
            evento.al_cuarto_fuste = al_cuarto_fuste
            evento.pe_primer_fuste = pe_primer_fuste
            evento.pe_segundo_fuste = pe_segundo_fuste
            evento.pe_tercer_fuste = pe_tercer_fuste
            evento.pe_cuarto_fuste = pe_cuarto_fuste
            evento.big_observaciones = big_observaciones
            evento.fecha_medicion = fecha_medicion
            evento.fecha_trabajo = fecha_trabajo
            evento.fecha_inicio = fecha_inicio
            evento.fecha_destoconado = fecha_destoconado
            evento.fecha_recoleccion = fecha_recoleccion
            evento.valor_intervencion = valor_intervencion
            evento.latitud = latitud
            evento.longitud = longitud

            numero_max = 0
            records = Evento.objects.all()
            #Loop through each record
            for record in records:
                field_as_int = int(record.numero)
                #print(field_as_int)
                if (field_as_int >= numero_max):
                    numero_max = field_as_int
            evento.numero = str(numero_max + 1)
            if len(request.FILES) != 0:
                evento.image = imagen
                evento.image_2 = imagen_2
                evento.image_3 = imagen_3
                evento.image.name = str(evento.numero)+ '_antes' + '.jpg'
                evento.image_2.name = str(evento.numero)+ '_durante' + '.jpg'
                evento.image_3.name = str(evento.numero)+ '_despues' + '.jpg'
            evento.save()
            if request.user == "D":
                return redirect('appointment:director-eventos')
            else:
                return redirect('appointment:student-eventos')




            """ evento = form.save(commit=False)
            evento.student = request.user
            evento.date = datetime.datetime.now()
            evento.ciudad = ciudad
            evento.tipo_arbol = arbol
            evento.lugar = destino
            evento.numero = numero
            evento.nombre_comun = nombre_comun
            evento.nombre_cientifico = nombre_cientifico
            evento.familia = familia
            evento.altura = altura
            evento.dap = dap
            evento.diametro_copa = diametro_copa
            evento.comuna = comuna
            evento.barrio = barrio
            evento.recomendaciones = recomendaciones
            evento.latitud = latitud
            evento.longitud = longitud
            numero_max = 0
            records = Evento.objects.all()
            #Loop through each record
            for record in records:
                field_as_int = int(record.numero)
                #print(field_as_int)
                if (field_as_int >= numero_max):
                    numero_max = field_as_int
            evento.numero = str(numero_max + 1)
            if len(request.FILES) != 0:
                evento.image = imagen
                evento.image.name = str(evento.numero)+'.jpg'
            evento.save()
            if request.user == "D":
                return redirect('appointment:director-eventos')
            else:
                return redirect('appointment:student-eventos') """
    else:
        form = EventoForm()
    return render(request, 'appointment/evento_create.html', {'form': form})

def get(self, request, *args, **kwargs):
 
        search_query = request.GET.get('search_box', 'nada')
        """
        print(search_query)
        acumulado = []
        if(search_query != 'None'):
            nombres =  list(search_query)
            cuenta = 0
            for id in nombres:
                if(id == ' '):
                    acumulado.append('_') 
                else:
                    acumulado.append(nombres[cuenta])
                cuenta += 1

        nombre_completo = ''.join(acumulado)
        print(nombre_completo)
        """
        coordenadas = "Coomeva"
        context = {
            'coordenadas' : coordenadas,
        }
        return render(request, 'appointment/urgencia.html', context)

class EventosForAstudentView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10
    
    def get_queryset(self):
        estudiante = self.request.user.id
        return Evento.objects.filter(student_id=estudiante).order_by('-numero')

class EventosForAdirectorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10

    def get_queryset(self):
        return Evento.objects.all().order_by('numero')
#############################################################################################

#############################################################################################


""" def EventoUpdate(request, pk):
    instance = Evento.objects.get(id=pk)
    form = EventoForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form': form,
        'instance': instance,
    }

    return render(request, 'evento_update.html', context) """




def EventoDetailView(request,*args, **kwargs):
    palabra = request.GET.get('value')
    numero_lote = int(palabra)

    detalle = Evento.objects.get(numero=numero_lote)

    codigo = detalle.codigo
    date = detalle.date
    numero = detalle.numero
    version = detalle.version
    direccion = detalle.direccion
    numero_concepto = detalle.numero_concepto
    localidad = detalle.localidad
    codigo_sigau = detalle.codigo_sigau
    no_arbol = detalle.no_arbol
    especie_vegetal = detalle.especie_vegetal
    tipo_manejo = detalle.tipo_manejo
    presencia_avifauna = detalle.presencia_avifauna
    manejo = detalle.manejo
    observaciones = detalle.observaciones
    al_primer_fuste = detalle.al_primer_fuste
    al_segundo_fuste = detalle.al_segundo_fuste
    al_tercer_fuste = detalle.al_tercer_fuste
    al_cuarto_fuste = detalle.al_cuarto_fuste
    pe_primer_fuste = detalle.pe_primer_fuste
    pe_segundo_fuste = detalle.pe_segundo_fuste
    pe_tercer_fuste = detalle.pe_tercer_fuste
    pe_cuarto_fuste = detalle.pe_cuarto_fuste
    big_observaciones, = detalle.big_observaciones,
    fecha_medicion = detalle.fecha_medicion
    fecha_trabajo = detalle.fecha_trabajo
    fecha_inicio = detalle.fecha_inicio
    fecha_destoconado = detalle.fecha_destoconado
    fecha_recoleccion = detalle.fecha_recoleccion
    valor_intervencion = detalle.valor_intervencion
    latitud = detalle.latitud
    longitud = detalle.longitud


    context = {
        'codigo' : codigo,
        'date' : date,
        'numero' : numero,
        'version' : version,
        'direccion' : direccion,
        'numero_concepto' : numero_concepto,
        'localidad' : localidad,
        'codigo_sigau' : codigo_sigau,
        'no_arbol' : no_arbol,
        'especie_vegetal' : especie_vegetal,
        'tipo_manejo' : tipo_manejo,
        'presencia_avifauna' : presencia_avifauna,
        'manejo' : manejo,
        'observaciones' : observaciones,
        'al_primer_fuste' : al_primer_fuste,
        'al_segundo_fuste' : al_segundo_fuste,
        'al_tercer_fuste' : al_tercer_fuste,
        'al_cuarto_fuste' : al_cuarto_fuste,
        'pe_primer_fuste' : pe_primer_fuste,
        'pe_segundo_fuste' : pe_segundo_fuste,
        'pe_tercer_fuste' : pe_tercer_fuste,
        'pe_cuarto_fuste' : pe_cuarto_fuste,
        'big_observaciones' : big_observaciones,
        'fecha_medicion' : fecha_medicion,
        'fecha_trabajo' : fecha_trabajo,
        'fecha_inicio' : fecha_inicio,
        'fecha_destoconado' : fecha_destoconado,
        'fecha_recoleccion' : fecha_recoleccion,
        'valor_intervencion' : valor_intervencion,
        'latitud' : latitud,
        'longitud' : longitud,
    }

    return render(request, 'evento_detail.html', context)


#############################################################################################

#############################################################################################
#CSV FILE
def some_view(request):
    palabra = request.GET.get('value')
    numero_lote = int(palabra)
    registro = Evento.objects.filter(numero=numero_lote)
    response = HttpResponse(content_type='text/csv')
    fecha =  str(datetime.datetime.now())
    #fecha = fecha + '.csv'
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'
    #response['Content-Disposition'] = 'attachment; filename=fecha'
    writer = csv.writer(response)
    writer.writerow([fecha,])
    writer.writerow(['Lista_de_eventos:',])
    writer.writerow([' ',])
    writer.writerow(['codigo', 'date', 'numero', 'version', 'direccion', 'numero_concepto', 'localidad', 'codigo_sigau', 'no_arbol', 'especie_vegetal', 'tipo_manejo', 'presencia_avifauna', 'manejo', 'observaciones', 'al_primer_fuste', 'al_segundo_fuste', 'al_tercer_fuste','al_cuarto_fuste','pe_primer_fuste','pe_segundo_fuste','pe_tercer_fuste','pe_cuarto_fuste','big_observaciones','fecha_medicion','fecha_trabajo','fecha_inicio','fecha_destoconado','fecha_recoleccion','valor_intervencion','latitud','longitud'])
    writer.writerow([' ',])
    cantidad = len(registro)
    for i in range(len(registro)):
        writer.writerow([registro[i]])
    writer.writerow([' ',])

    """ eventos = Evento.objects.all().order_by('date')
    cantidad = len(eventos)
    for i in range(len(eventos)):
        writer.writerow([eventos[i]])
    writer.writerow([' ',]) """
    return response
#############################################################################################

#############################################################################################
##PDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

## form necesaria para los posts de PDF
class AvailabilityForm(forms.Form):
    ingreso = forms.CharField(required=True)

#PDF ACTIVIDADES
class ActividadPDF(View):
    def get(self, request, *args, **kwargs):
        citas = Prescription.objects.all().order_by('date')
        actividades = Prescription.objects.all().order_by('-date')
        context = {
            'citas' : citas,
            'actividades' : actividades,
        }

        pdf = render_to_pdf('appointment/pdf_actividad.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
    
    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            forma = form.cleaned_data
            forma = str(forma)
            palabra = forma.split(':')
            palabra = palabra[1]
            frase = list(palabra)
            caballo = frase[2:-2]
            caballo = ''.join(caballo)
        
        flag_actividad = 0
        if caballo == 'valentina':
            id_caballo = 2
        elif caballo == 'roberta':
            id_caballo = 5
        elif caballo == 'totti':
            id_caballo = 3
        elif caballo == 'sebastian':
            id_caballo = 4
        elif caballo == 'todos':
            flag_actividad = 1
        else:
            pass

        if(flag_actividad):
            
            caballo_actividades = Prescription.objects.all().order_by('-date')
            flag_actividad = 0
        else:
            caballo_actividades = Prescription.objects.filter(student_id=id_caballo)

        context = {
            'caballo_actividades' : caballo_actividades,
            'flag_actividad' : flag_actividad,
        }
        pdf = render_to_pdf('appointment/pdf_actividad.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
#############################################################################################

#PDF EVENTOS
class EventoPDF(View):
    def get(self, request, *args, **kwargs):
        palabra = request.GET.get('value')
        numero_lote = int(palabra)
        registro = Evento.objects.filter(numero=numero_lote)
        nombre_foto = ''
        nombre_foto_2 = ''
        nombre_foto_3 = ''
        nombre_foto = Evento.objects.get(numero=numero_lote).image
        nombre_foto_2 = Evento.objects.get(numero=numero_lote).image_2
        nombre_foto_3 = Evento.objects.get(numero=numero_lote).image_3

        citas = Evento.objects.all().order_by('date')
        actividades = Evento.objects.all().order_by('-date')
        context = {
            'registro' : registro,
            'nombre_foto' : nombre_foto,
            'nombre_foto_2' : nombre_foto_2,
            'nombre_foto_3' : nombre_foto_3,
            'citas' : citas,
            'actividades' : actividades,
        }

        pdf = render_to_pdf('appointment/pdf_evento.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
    
    def post(self, request, *args, **kwargs):
        check_box = ''
        eventos = ''
        nombre_foto = ''
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            forma = form.cleaned_data
            forma = str(forma)
            check_box = request.POST.get('ingreso', None)
            nombre_foto = 'arbol.jpeg'
            #print(check_box)
            if (check_box != 'None'):
                eventos = Evento.objects.filter(numero=check_box)
                nombre_foto = Evento.objects.get(numero=check_box).image
                
        if (check_box != None):
            context = {
                'eventos' : eventos,
                'nombre_foto' : nombre_foto,
            }
        else:
            context = {
                'nombre_foto' : nombre_foto,
            }
        #pdf = render_to_pdf('appointment/pdf_evento.html', context)

        # create csc instead of pdf of selected event
        response = HttpResponse(content_type='text/csv')
        fecha =  str(datetime.datetime.now())
        response['Content-Disposition'] = 'attachment; filename="datos.csv"'
        writer = csv.writer(response)
        writer.writerow([fecha,])
        writer.writerow(['Lista_de_eventos:',])
        writer.writerow([' ',])
        writer.writerow(['date', 'actividad', 'lugar', 'ciudad', 'tipo_arbol', 'numero', 'nombre_comun', 'nombre_cientifico', 'familia', 'altura', 'dap', 'diametro_copa', 'comuna', 'barrio', 'recomendaciones', 'latitud', 'longitud',])
        writer.writerow([' ',])

        if (check_box != 'None'):
                eventos = Evento.objects.filter(numero=check_box)
                for i in range(len(eventos)):
                    writer.writerow([eventos[i]])
                writer.writerow([' ',])
        return response
        #

        #return HttpResponse(pdf, content_type='application/pdf')

#############################################################################################
#URGENCIA



class UrgenciaForAdirectorView(LoginRequiredMixin, View):
    
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10
    
    

    def get(self, request, *args, **kwargs):
 
        search_query = request.GET.get('search_box', 'nada')
        latlong = request.GET.get('latlong', None)
        atencion = request.GET.get('atencion_submit',None)
        ambulancia = request.GET.get('ambulancia_submit',None)
        #print (ambulancia)
        #print (atencion)
        #print (acudiente)
        #print(latlong)
        print(search_query)
        id_buscar = 2
        acumulado = []
        if(search_query != 'None'):
            nombres =  list(search_query)
            cuenta = 0
            for id in nombres:
                if(id == ' '):
                    acumulado.append('_') 
                else:
                    acumulado.append(nombres[cuenta])
                cuenta += 1

        nombre_completo = ''.join(acumulado)
        print(nombre_completo)

        try:
            usuarios = User.objects.get(username=nombre_completo)
        except:
            usuarios = User.objects.get(username="valentina")
        print(usuarios.id)
        id_buscar =usuarios.id

        ambulancia_name = ""
        puntos_atencion = ""
        imagen = ""
        notas = ""
        actividades = ""
        mapa_cali = "../static/images/mapa_cali.png"

        if id_buscar != 2:
            usuario = UserProfile.objects.get(user=id_buscar)
            ambulancia_name = usuario.identidad_seguro
            notas = Nota.objects.filter(student_id=id_buscar).order_by('-date')
            actividades = Prescription.objects.filter(student_id=id_buscar).order_by('-date')
            imagen = "../static/images/valentina.jpeg"

            ############################
            #actualiza quien y cuando busco el perfil, por deafult tiene que estar ';' 
            ###########################
            now = datetime.datetime.now()
            now = str(now)
            ahora = now.split(' ')
            hora = ahora[1].split('.')

            toUpdate = usuario.busqueda 
            toUpdate = toUpdate + ' ' + str(ahora[0]) + ' ' + str(hora[0]) + ' ' + str(request.user)+ ' ; ' 
            UserProfile.objects.filter(user=id_buscar).update(busqueda=str(toUpdate))
            
            
        else:
            usuario = ""

        if ambulancia_name == "SALUD TOTAL":
            ambulancia_name = "6640235"
            puntos_atencion = "la flora, centenario"
        else:
            puntos_atencion = ""
        if ambulancia == "None":
            ambulancia_name = ""

        coordenadas ="Coomeva"

        uno = 1

        print(coordenadas)

        context = {
            'usuario' : usuario,
            'imagen' : imagen,
            'ambulancia_name' : ambulancia_name,
            'puntos_atencion' : puntos_atencion,
            'notas' : notas,
            'actividades' : actividades,
            'mapa_cali': mapa_cali,
            'uno' : uno,
            'coordenadas' : coordenadas,
        }
        return render(request, 'appointment/urgencia.html', context)

   
    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('your_name', None)
        ubicacion_query = request.POST.get('your_lat', None)
        print(search_query)
        print(ubicacion_query)

    

        lunes = 2
        martes = 3
        context = {
                'lunes' : lunes,
                'martes' : martes,
            }
        return render(request, 'appointment/urgencia.html',context)
    
