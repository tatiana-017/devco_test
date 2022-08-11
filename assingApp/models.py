from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def _create_assing(self,serial,name,typeProduc,system,
    ownerName,ownerEmail,date):
        assing = self.model(
            serial = serial,
            name = name,
            typeProduc = typeProduc,
            system = system,
            ownerName = ownerName,
            ownerEmail = ownerEmail,
            date = date
        )
        return assing
    def create_assing(self,serial,name,typeProduc,system,ownerName,ownerEmail,date):
        return self._create_assing(serial,name,typeProduc,system,ownerName,ownerEmail,date)


class assing(models.Model):
    serial=models.IntegerField()
    name=models.CharField(max_length=50)
    typeProduc=models.CharField(max_length=50)
    system=models.CharField(max_length=50)
    ownerName=models.CharField(max_length=70)
    ownerEmail=models.EmailField()
    date=models.DateField()
    objects = UsuarioManager()

    class Meta:
        verbose_name="assing"
        verbose_name_plural="assignments"
    
    def __str__(self):
        return self.serial
