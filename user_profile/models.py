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
    ('SD', 'SD'),
]

GRADO = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('01 ACADEMICO', '01 ACADEMICO'),
    ('02 ACADEMICO', '02 ACADEMICO'),
    ('03 ACADEMICO', '03 ACADEMICO'),
    ('04 ACADEMICO', '04 ACADEMICO'),
    ('05 ACADEMICO', '05 ACADEMICO'),
]

SECCION = [
    ('1','01'),
    ('2','02'),
    ('3', '03'),
]

JORNADA = [
    ('MANANA', 'MANANA'),
    ('TARDE' , 'TARDE'),
]

TIPO_DOCUMENTO = [
    ('NIP', 'NIP'),
    ('NUIP', 'NUIP'),
    ('OTRO', 'OTRO'),
    ('R.C', 'R.C'),
    ('T.I', 'T.I'),
]

SEGURO = [
    ('ASMESALUD', 'ASMESALUD'),
    ('CAFESALUD', 'CAFESALUD'),
    ('CAPRECOM' , 'CAPRECOM'),
    ('CEDIMA' , 'CEDIMA'),
    ('COLSANITAS' , 'COLSANITAS'),
    ('COMFAMILIAR', 'COMFAMILIAR'),
    ('COMFENALCO' , 'COMFENALCO'),
    ('COOSALUD' , 'COOSALUD'),
    ('COOMEVA' , 'COOMEVA'),
    ('COSMITET' , 'COSMITET'),
    ('CRUZ BLANCA', 'CRUZ BLANCA'),
    ('EMAVI' , 'EMAVI'),
    ('EMSANAR' , 'EMSANAR'),
    ('LA POLICIA', 'LA POLICIA'),
    ('MEDIMAS' , 'MEDIMAS'),
    ('NUEVA EPS', 'NUEVA EPS'),
    ('P.N.C' , 'P.N.C'),
    ('PONAL', 'PONAL'),
    ('PREVISORA', 'PREVISORA'),
    ('S.O.S' , 'S.O.S'),
    ('SALUD TOTAL' , 'SALUD TOTAL'),
    ('SALUDCOOP' , 'SALUDCOOP'),
    ('SANIDAD MILITAR' , 'SANIDAD MILITAR'),
    ('SANITAS' , 'SANITAS'),
    ('SIN DEFINIR' , 'SIN DEFINIR'),
    ('SISBEN' , 'SISBEN'),
    ('SURAMERICANA' , 'SURAMERICANA'),
]

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True, blank=True, max_length=8)
    nombre_estudiante = models.CharField(max_length=50 , blank=True ,null=True)
    nombre_2_estudiante = models.CharField(max_length=50 , blank=True ,null=True)
    apellido_estudiante = models.CharField(max_length=50, blank=True,null=True)
    apellido_2_estudiante = models.CharField(max_length=50, blank=True,null=True)
    tipodoc_estudiante = models.CharField(choices=TIPO_DOCUMENTO, max_length=4, blank=True , default='T.I')
    nit_estudiante = models.CharField(max_length=50, blank=True,null=True)
    cumpleanos_estudiante = models.CharField(max_length=50, blank=True,null=True)
    direccion_estudiante = models.CharField(max_length=50, blank=True,null=True)
    grado_estudiante = models.CharField(choices=GRADO, max_length=12, blank=True , default='01')
    seccion_estudiante = models.CharField(choices=SECCION, max_length=1, blank=True , default='1')
    jornada_estudiante = models.CharField(choices=JORNADA, max_length=6, blank=True , default='MANANA')
    id_estudiante = models.CharField(max_length=50, blank=True,null=True)
    telefono_estudiante = models.CharField(max_length=50, blank=True,null=True)
    id_seguro = models.CharField(max_length=50, blank=True,null=True)
    identidad_seguro = models.CharField(choices=SEGURO, max_length=15, blank=True , default='Coomeva')
    descripcion_seguro = models.CharField(max_length=50, blank=True,null=True)
    condicion_especial = models.CharField(max_length=50, blank=True,null=True)
    descripcion_condicion_especial = models.CharField(max_length=50, blank=True,null=True)
    nombre_papa = models.CharField(max_length=50, blank=True,null=True)
    direccion_papa = models.CharField(max_length=50, blank=True,null=True)
    ocupacion_papa = models.CharField(max_length=50, blank=True,null=True)
    nombre_mama = models.CharField(max_length=50, blank=True,null=True)
    direccion_mama = models.CharField(max_length=50, blank=True,null=True)
    ocupacion_mama = models.CharField(max_length=50, blank=True,null=True)
    nombre_acudiente = models.CharField(max_length=50, blank=True,null=True)
    nombre_2_acudiente = models.CharField(max_length=50, blank=True,null=True)
    apellido_acudiente = models.CharField(max_length=50, blank=True,null=True)
    apellido_2_acudiente = models.CharField(max_length=50, blank=True,null=True)
    cedula_acudiente = models.CharField(max_length=50, blank=True,null=True)
    cumpleanos_acudiente = models.CharField(max_length=50, blank=True,null=True)
    email_acudiente = models.CharField(max_length=50, blank=True,null=True)
    direccion_acudiente = models.CharField(max_length=50, blank=True,null=True)
    parentesco_acudiente = models.CharField(max_length=50, blank=True,null=True)
    celular_acudiente = models.CharField(max_length=50, blank=True,null=True)
    busqueda = models.CharField(max_length=300, blank=True,null=True)

   
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.user, 
        self.name , 
        self.gender, 
        self.blood_group, 
        self.status, 
        self.nombre_estudiante, 
        self.nombre_2_estudiante, 
        self.apellido_estudiante, 
        self.apellido_2_estudiante, 
        self.tipodoc_estudiante , 
        self.nit_estudiante , 
        self.cumpleanos_estudiante ,
        self.direccion_estudiante, 
        self.grado_estudiante,
        self.seccion_estudiante, 
        self.jornada_estudiante, 
        self.id_estudiante,
        self.telefono_estudiante , 
        self.id_seguro , 
        self.identidad_seguro ,
        self.descripcion_seguro , 
        self.condicion_especial  , 
        self.descripcion_condicion_especial,
        self.nombre_papa,
        self.direccion_papa, 
        self.ocupacion_papa,
        self.nombre_mama , 
        self.direccion_mama,
        self.ocupacion_mama , 
        self.nombre_acudiente , 
        self.nombre_2_acudiente , 
        self.apellido_acudiente, 
        self.apellido_2_acudiente, 
        self.cedula_acudiente , 
        self.cumpleanos_acudiente , 
        self.email_acudiente , 
        self.parentesco_acudiente , 
        self.direccion_acudiente, 
        self.celular_acudiente,
        self.busqueda
         )

