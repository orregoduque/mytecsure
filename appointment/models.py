from socket import NI_NUMERICHOST
from django.db import models
from django.contrib.auth import get_user_model
from django.conf.urls.static import static
User = get_user_model()

class Prescription(models.Model):
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='director_id', default='director')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_id', default='student')
    date = models.DateField(auto_now_add=True)
    estado = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10,  default='Pending')
    sintomas = models.CharField(max_length=200, default= 'fiebre')
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.student, self.date, self.sintomas, self.estado)

class Nota(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_idddd', default='student')
    date = models.DateField()
    actividad = models.CharField(max_length=300, default= 'concurso ')
    
    @property
    def students(self):
        return "{}".format(self.student)

    def __str__(self):
        return "{}-{}-{}".format(self.student, self.date,self.actividad)



LUGAR = [
    ('Parque', 'Parque'),
    ('Colegio', 'Colegio'),
    ('Universidad', 'Universidad'),
    ('Rural', 'Rural'),
    ('Barrio', 'Barrio'),
    ('Campo Deportivo', 'Campo Deportivo'),
]

CIUDAD = [ 
    ('Cali', 'Cali'),
    ('Bogota', 'Bogota'),
    ('Medellin', 'Medellin'),
    ('Barranquilla ', 'Barranquilla '),
]

TIPOS_ARBOL = [
    ('PALMA', 'PALMA'),
    ('BONSAI', 'BONSAI'),
    ('GIRASOL', 'GIRASOL'),
]

MOTIVACION = [
    ('SIEMBRA', 'SIEMBRA'),
    ('RIEGO', 'RIEGO'),
    ('ABONO', 'ABONO'),
]

AVIFAUNA = [
    ('SI', 'SI'),
    ('NO', 'NO'),
]

class Evento(models.Model):
    """ student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_idd', default='student')
    date = models.DateField()
    actividad = models.CharField(choices=MOTIVACION, max_length=7, default= 'SIEMBRA')
    lugar = models.CharField(choices=LUGAR, max_length=16, default='Parque')
    ciudad = models.CharField(choices=CIUDAD, max_length=13, default= 'Cali')
    tipo_arbol = models.CharField(choices=TIPOS_ARBOL, max_length=7, default='PALMA')
    image = models.ImageField( null=True , blank= True)
    numero = models.CharField(max_length=20, blank=True)
    nombre_comun = models.CharField(max_length=100, blank=True)
    nombre_cientifico = models.CharField(max_length=100, blank=True)
    familia = models.CharField(max_length=100, blank=True)
    altura = models.CharField(max_length=20, blank=True)
    dap = models.CharField(max_length=20, blank=True)
    diametro_copa = models.CharField(max_length=20, blank=True)
    comuna = models.CharField(max_length=20, blank=True)
    barrio = models.CharField(max_length=20, blank=True)
    recomendaciones = models.CharField(max_length=200, blank=True)
    latitud = models.CharField(max_length=20, blank=True)
    longitud = models.CharField(max_length=20, blank=True) """

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_idd', default='student')
    date = models.DateField()
    image = models.ImageField( null=True , blank= True)
    image_2 = models.ImageField( null=True , blank= True)
    image_3 = models.ImageField( null=True , blank= True)
    numero = models.CharField(max_length=20, blank=True)
    codigo = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    numero_concepto = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    localidad = models.CharField(max_length=100, blank=True)
    codigo_sigau = models.CharField(max_length=100, blank=True)
    no_arbol = models.CharField(max_length=100, blank=True)
    especie_vegetal = models.CharField(max_length=100, blank=True)
    tipo_manejo = models.CharField(max_length=100, blank=True)
    presencia_avifauna = models.CharField(choices=AVIFAUNA, max_length=2, default='SI')
    manejo = models.CharField(max_length=100, blank=True)
    observaciones = models.CharField(max_length=100, blank=True)
    al_primer_fuste = models.CharField(max_length=100, blank=True)
    al_segundo_fuste = models.CharField(max_length=100, blank=True)
    al_tercer_fuste = models.CharField(max_length=100, blank=True)
    al_cuarto_fuste = models.CharField(max_length=100, blank=True)
    pe_primer_fuste = models.CharField(max_length=100, blank=True)
    pe_segundo_fuste = models.CharField(max_length=100, blank=True)
    pe_tercer_fuste = models.CharField(max_length=100, blank=True)
    pe_cuarto_fuste = models.CharField(max_length=100, blank=True)
    big_observaciones = models.CharField(max_length=100, blank=True)
    fecha_medicion = models.CharField(max_length=100, blank=True)
    fecha_trabajo = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.CharField(max_length=100, blank=True)
    fecha_destoconado = models.CharField(max_length=100, blank=True)
    fecha_recoleccion = models.CharField(max_length=100, blank=True)
    valor_intervencion = models.CharField(max_length=100, blank=True)
    latitud = models.CharField(max_length=20, blank=True)
    longitud = models.CharField(max_length=20, blank=True)
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        """ return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.date, 
        self.actividad, 
        self.lugar, 
        self.ciudad, 
        self.tipo_arbol, 
        self.numero, 
        self.nombre_comun, 
        self.nombre_cientifico, 
        self.familia, 
        self.altura, 
        self.dap, 
        self.diametro_copa, 
        self.comuna, 
        self.barrio, 
        self.recomendaciones, 
        self.latitud, 
        self.longitud) """



        return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.codigo,
        self.date,
        self.numero,
        self.version,
        self.direccion,
        self.numero_concepto,
        self.localidad,
        self.codigo_sigau,
        self.no_arbol,
        self.especie_vegetal,
        self.tipo_manejo,
        self.presencia_avifauna,
        self.manejo,
        self.observaciones,
        self.al_primer_fuste,
        self.al_segundo_fuste,
        self.al_tercer_fuste,
        self.al_cuarto_fuste,
        self.pe_primer_fuste,
        self.pe_segundo_fuste,
        self.pe_tercer_fuste,
        self.pe_cuarto_fuste,
        self.big_observaciones, 
        self.fecha_medicion,
        self.fecha_trabajo,
        self.fecha_inicio,
        self.fecha_destoconado,
        self.fecha_recoleccion,
        self.valor_intervencion,
        self.latitud,
        self.longitud)
