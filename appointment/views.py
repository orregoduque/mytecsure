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
            username = form.cleaned_data.get("student")
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
            imagen = request.FILES["image"]
            
            evento = form.save(commit=False)
            evento.student = request.user
            #evento.director = request.user
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
            evento.image = imagen
            evento.save()
            if request.user == "D":
                return redirect('appointment:director-eventos')
            else:
                return redirect('appointment:student-eventos')
    else:
        form = EventoForm()
    return render(request, 'appointment/evento_create.html', {'form': form})

def get(self, request, *args, **kwargs):
 
        search_query = request.GET.get('search_box', 'nada')
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
        return Evento.objects.filter(student_id=estudiante).order_by('date')

class EventosForAdirectorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10

    def get_queryset(self):
        return Evento.objects.all().order_by('date')
#############################################################################################

#############################################################################################
#CSV FILE
def some_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="citas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Lista_de_citas:',])
    writer.writerow([' ',])
    writer.writerow(['Caballo', 'Fecha', 'Estado', 'Asunto'])
    citas = Prescription.objects.all().order_by('date')
    writer.writerow(citas)
    writer.writerow([' ',])
    writer.writerow(['Lista_de_actividades:',])
    writer.writerow([' ',])
    writer.writerow(['Caballo', 'Fecha', 'Comida', 'Caminadora','Pasto','Herradura'])
    actividades = Prescription.objects.all().order_by('-date')
    writer.writerow(actividades)
    
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
        citas = Evento.objects.all().order_by('date')
        actividades = Evento.objects.all().order_by('-date')
        context = {
            'citas' : citas,
            'actividades' : actividades,
        }

        pdf = render_to_pdf('appointment/pdf_evento.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
    
    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            forma = form.cleaned_data
            forma = str(forma)
            eventos = Evento.objects.all().order_by('-date')
        context = {
            'eventos' : eventos,
        }
        pdf = render_to_pdf('appointment/pdf_evento.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

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
    
