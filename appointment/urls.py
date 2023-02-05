from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "appointment"

urlpatterns = [
    path("prescriptions/s/", views.PrescriptionStudentView.as_view(), name="student-prescriptions"),
    path("prescriptions/d/", views.PrescriptionListView.as_view(), name="doc-prescriptions"),
    path("prescription/create", views.PrescriptionCreateView, name="doc-prescriptions-create"),
    path("prescription/d/<int:id>/", views.prescription_edit, name="prescription_edit"),
    path("rdashboard/", views.rdashboard, name="r_dashboard"),
    path("hrdashboard/", views.hrdashboard, name="hr_dashboard"),
    path("hraccounting/", views.hraccounting, name="hr_accounting"),
    path('csv_view/', views.some_view, name="csv_view"),
    path("nota/create", views.NotaCreateView, name="nota-create"),
    path("notas/s/", views.NotasForAstudentView.as_view(), name="student-notas"),
    path("notas/d/", views.NotasForAdirectorView.as_view(), name="director-notas"),
    path('pdf_actividad/', views.ActividadPDF.as_view(), name="pdf_actividad"),
    path('pdf_evento/', views.EventoPDF.as_view(), name="pdf_evento"),
    path("evento/create", views.EventoCreateView, name="evento-create"),
    #path("evento/update/<int:pk>/", views.EventoUpdate, name="evento-update"),
    path("eventos/s/", views.EventosForAstudentView.as_view(), name="student-eventos"),
    path("eventos/d/", views.EventosForAdirectorView.as_view(), name="director-eventos"),
    path("urgencia/", views.UrgenciaForAdirectorView.as_view(), name="director-urgencia"),
    path('evento/detail/', views.EventoDetailView, name='Evento-DetailView'),
]
