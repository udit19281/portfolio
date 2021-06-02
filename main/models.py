from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    image=models.URLField(max_length=200,default='http://www.foo.com')
    link=models.URLField(max_length=200)

    def __str__(self):
        return self.name



