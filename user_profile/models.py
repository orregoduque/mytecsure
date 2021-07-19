from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
User = get_user_model()

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

BLOOD_GROUPS = [
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
]

GRADO = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
]

SEGURO = [
    ('Colsanitas', 'Colsanitas'),
    ('Coomeva', 'Coomeva'),
    ('Seguro Social', 'Seguro Social'),
    ('Imbanaco', 'Imbanaco'),
    ('Ninguno', 'Ninguno'),
]

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True, blank=True, max_length=8)
    nombre_estudiante = models.CharField(max_length=50 , blank=True ,null=True)
    apellido_estudiante = models.CharField(max_length=50, blank=True,null=True)
    nit_estudiante = models.CharField(max_length=50, blank=True,null=True)
    cumpleanos_estudiante = models.CharField(max_length=50, blank=True,null=True)
    email_estudiante = models.CharField(max_length=50, blank=True,null=True)
    direccion_estudiante = models.CharField(max_length=50, blank=True,null=True)
    barrio_estudiante = models.CharField(max_length=50, blank=True,null=True)
    comuna_estudiante = models.CharField(max_length=50, blank=True,null=True)
    grado_estudiante = models.CharField(choices=GRADO, max_length=2, blank=True , default='1')
    id_estudiante = models.CharField(max_length=50, blank=True,null=True)
    nombre_acudiente = models.CharField(max_length=50, blank=True,null=True)
    apellido_acudiente = models.CharField(max_length=50, blank=True,null=True)
    cedula_acudiente = models.CharField(max_length=50, blank=True,null=True)
    cumpleanos_acudiente = models.CharField(max_length=50, blank=True,null=True)
    email_acudiente = models.CharField(max_length=50, blank=True,null=True)
    direccion_acudiente = models.CharField(max_length=50, blank=True,null=True)
    barrio_acudiente = models.CharField(max_length=50, blank=True,null=True)
    comuna_acudiente = models.CharField(max_length=50, blank=True,null=True)
    trabajo_acudiente = models.CharField(max_length=50, blank=True,null=True)
    celular_acudiente = models.CharField(max_length=50, blank=True,null=True)
    id_seguro = models.CharField(max_length=50, blank=True,null=True)
    identidad_seguro = models.CharField(choices=SEGURO, max_length=13, blank=True , default='Coomeva')
    descripcion_seguro = models.CharField(max_length=50, blank=True,null=True)
    condicion_especial = models.CharField(max_length=50, blank=True,null=True)
    descripcion_condicion_especial = models.CharField(max_length=50, blank=True,null=True)

    """
   
    seguro
    alergias
    cirugias
    medicamentos
     """
   

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.user, self.name , self.gender, 
        self.blood_group , self.status , self.nombre_estudiante, self.apellido_estudiante, self.nit_estudiante , self.cumpleanos_estudiante ,
        self.email_estudiante,self.direccion_estudiante, self.barrio_estudiante , self.comuna_estudiante, self.grado_estudiante, self.id_estudiante,
        self.nombre_acudiente , self.apellido_acudiente, self.cedula_acudiente , self.cumpleanos_acudiente , self.email_acudiente , 
        self.direccion_acudiente, self.barrio_acudiente, self.comuna_acudiente , self.trabajo_acudiente , self.celular_acudiente, 
        self.id_seguro , self.identidad_seguro ,self.descripcion_seguro , self.condicion_especial  , self.descripcion_condicion_especial )

