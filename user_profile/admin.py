from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(UserProfile)

class FilterUserProfile(admin.ModelAdmin):
    list_display =('user','grado_estudiante', 'identidad_seguro','status', 'nombre_acudiente')
    list_filter = ('grado_estudiante' , 'identidad_seguro','status')
admin.site.register(UserProfile,FilterUserProfile)



