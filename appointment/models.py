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

COORDENADAS = [ 
    ('Colombo', '3.337044-76.543025'),
    ('Americano', '3.378298-76.544850'),
    ('Frances', '3.486792-76.521890'),
    ('Bolivar', '3.340611-76.546607'),
    ('Finca', '3.220535-76.582756'),
    ('Teatro', '3.449569-76.535987'),
    ('Imbanaco', '3.426507-76.544942'),
    ('Colsanitas', '3.454529-76.537065'),
    ('Coomeva', '3.464280-76.531116'),
    ('Seguro Social', '3.467319-76.524384'),
]

class Evento(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_idd', default='student')
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='director_idd', default='director')
    date = models.DateField()
    actividad = models.CharField(max_length=300, default= 'interclases')
    lugar = models.CharField(choices=LUGAR, max_length=9, blank=True)
    hospital_cercano = models.CharField(max_length=300, default= 'Imbanaco')
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.student, self.date, self.actividad, self.lugar, self.hospital_cercano)
