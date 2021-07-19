from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext
from .models import * 
from .forms import * 
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import UserProfile
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

HOSPITAL_Colsanitas = [
    ('Imbanaco', '3.426507-76.544942'),
    ('Colsanitas', '3.454529-76.537065'),
    ('Coomeva', '3.464280-76.531116'),
    ('Seguro Social', '3.467319-76.524384'),
]

HOSPITAL_Coomeva = [
    ('Imbanaco', '3.426507-76.544942'),
    ('Colsanitas', '3.454529-76.537065'),
    ('Coomeva', '3.464280-76.531116'),
    ('Seguro Social', '3.467319-76.524384'),
]
HOSPITAL_Seguro = [
    ('Imbanaco', '3.426507-76.544942'),
    ('Colsanitas', '3.454529-76.537065'),
    ('Coomeva', '3.464280-76.531116'),
    ('Seguro Social', '3.467319-76.524384'),
]
HOSPITAL_Imbanaco = [
    ('Imbanaco', '3.426507-76.544942'),
    ('Colsanitas', '3.454529-76.537065'),
    ('Coomeva', '3.464280-76.531116'),
    ('Seguro Social', '3.467319-76.524384'),
]
@login_required(login_url='/login/')
def EventoCreateView(request):
    
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            #obtener usuario y su seguro
            #obtener destino

            #obtener coordenadas hospitales validos****
            #obtener coordenadas destino
            #hacer loop
            #calcular hospital mas cercano
            
            #distancia = (x2-x1)**2 + (y2-y1)**2
            #distancia = distancia**0.5


            """
            https://yari-demos.prod.mdn.mozit.cloud/en-US/docs/web/api/geolocation_api/using_the_geolocation_api/_sample_.Examples.html
            en la pestana de eventos,
            profesor selecciona estudiante, y boton para hacer la busqueda del hospital mas cercano
            basado en el seguro del estudiante
            y la posicion actual segun google maps
            un post con:

            username = form.cleaned_data.get("student")
            destino = form.cleaned_data.get("lugar")
            seguro = UserProfile.objects.get(user=username)
            idseguro = str(seguro)
            seguro = idseguro.split('-')
            eps = seguro[-4]

            falta:
            integrar api de google maps
            obtener coordenadas actuales
            calcular hospital mas cercano
            mostrar el mapa como llegar

            en lugar de calcular sobre la misma app
            un href con la direccion a ir, y que abra la app de google maps
            **indicar que se debe descargar la app de google maps

            dar la opcion de crear registro para evento a futuro (ninos pequenos), o evento inmediato
            alertar con un correo al padre, cuando se cree un registro de su hijo


            por ahora tener solo 2 modelos
            el de urgencia:
                seleccionando el nino y la ubicacion del celular, calcular hospital mas cercano

            el de ver perfil del hijo, y estudiante

            hacer una barra de busqueda para encontrar al estudiante o por nombre o por nit
            """
            username = form.cleaned_data.get("student")
            destino = form.cleaned_data.get("lugar")
            seguro = UserProfile.objects.get(user=username)
            idseguro = str(seguro)
            seguro = idseguro.split('-')
            eps = seguro[-4]
            print(username)
            print(destino)
            print(eps)
            cercano = 'Coomeva'
            #
            evento = form.save(commit=False)
            evento.director = request.user
            evento.date = datetime.datetime.now()
            evento.hospital_cercano = cercano
            evento.save()
            return redirect('appointment:director-eventos')
    else:
        form = EventoForm()
    return render(request, 'appointment/evento_create.html', {'form': form})


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

        pdf = render_to_pdf('appointment/pdf_factura.html', context)
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

#############################################################################################
#NEAREST HOSPITAL



class UrgenciaForAdirectorView(LoginRequiredMixin, View):
    
    login_url = '/login/'
    redirect_field_name = 'account:login'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
 
        search_query = request.GET.get('search_box', None)
        latlong = request.GET.get('latlong', None)
        print(latlong)
        print(search_query)
        id_buscar = 2
        if search_query == 'totti':
            id_buscar = 3;
        seguro = UserProfile.objects.get(user=id_buscar)
        #print(seguro)
        lunes = 2
        martes = 3
        context = {
            'lunes' : lunes,
            'martes' : martes,
            'seguro' : seguro,
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
    
