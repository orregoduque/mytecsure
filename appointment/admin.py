from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = 'TecSure Dashboard'
admin.site.site_title = 'TecSure Dashboard'

#admin.site.register(Prescription)
#admin.site.register(Nota)


class FilterPrescription(admin.ModelAdmin):
    list_display =('student','date', 'sintomas', 'estado')
    list_filter = ('student' , 'date', 'estado')
admin.site.register(Prescription,FilterPrescription)


class FilterNota(admin.ModelAdmin):
    list_display =('date', 'student','actividad')
    list_filter = ('date' , 'student')
admin.site.register(Nota,FilterNota)

class FilterEvento(admin.ModelAdmin):
    list_display =('student','date', 'lugar', 'actividad')
    list_filter = ('student' , 'date','lugar')
admin.site.register(Evento,FilterEvento)