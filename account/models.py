from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

USER_CHOICES = [
    ('D', 'Director'),
    ('S', 'Student'),
    ('P', 'Profesor'),
    ('HR', 'HR')
]

class User(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=2)

    def is_director(self):
        if self.user_type == 'D':
            return True
        else:
            return False

    def is_student(self):
        if self.user_type == 'S':
            return True
        else:
            return False

    def is_profesor(self):
        if self.user_type == 'P':
            return True
        else:
            return False

    def is_HR(self):
        if self.user_type == 'HR':
            return True
        else:
            return False

    class Meta:
        ordering = ('id',)
