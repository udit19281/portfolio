from django.db import models

# Create your models here.

class Project(models.Model):
    choi=[
        ('cabin','cabin'),
        ('cake','cake'),
        ('circus','circus'),
        ('game','game'),
        ('safe','safe'),
        ('submarine','submarine')
    ]
    name = models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    image=models.CharField(max_length=10,choices=choi)

    def __str__(self):
        return self.name



