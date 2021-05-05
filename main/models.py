from django.db import models

# Create your models here.

class Project(models.Model):
    choi=[
        ('1','cabin'),
        ('2','cake'),
        ('6','circus'),
        ('5','game'),
        ('4','safe'),
        ('3','submarine'),
        ('7','linux'),
        ('8','color switch'),
        ('9','python'),
        ('10','smart shoe')
    ]
    name = models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    image=models.CharField(max_length=20,choices=choi)

    def __str__(self):
        return self.name



