from django.db import models
from django.contrib.auth import get_user_model
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
    ('Colombo', 'Colombo'),
    ('Americano', 'Americano'),
    ('Frances', 'Frances'),
    ('Bolivar', 'Bolivar'),
    ('Finca', 'Finca'),
    ('Teatro', 'Teatro'),
]

HOSPITAL = [ 
    ('Imbanaco', 'Imbanaco'),
    ('Colsanitas', 'Colsanitas'),
    ('Coomeva', 'Coomeva'),
    ('Seguro Social', 'Seguro Social'),
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

class Evento(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_idd', default='student')
    #director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='director_idd', default='director')
    date = models.DateField()
    actividad = models.CharField(choices=MOTIVACION, max_length=7, default= 'interclases')
    lugar = models.CharField(choices=LUGAR, max_length=9, default='Colombo')
    hospital_cercano = models.CharField(max_length=300, default= 'Imbanaco')
    tipo_arbol = models.CharField(choices=TIPOS_ARBOL, max_length=7, default='PALMA', blank=True)
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        #return "{}-{}-{}-{}-{}-{}".format(self.student, self.date, self.actividad, self.lugar, self.hospital_cercano, self.tipo_arbol)
        return "{}-{}-{}-{}-{}".format(self.date, self.actividad, self.lugar, self.hospital_cercano, self.tipo_arbol)
