from django.db import models

# Create your models here.

class assing(models.Model):
    serial=models.IntegerField()
    name=models.CharField(max_length=50)
    typeProduc=models.CharField(max_length=50)
    system=models.CharField(max_length=50)
    ownerName=models.CharField(max_length=70)
    ownerEmail=models.EmailField()
    date=models.DateField()

    class Meta:
        verbose_name="assing"
        verbose_name_plural="assignments"
    
    def __str__(self):
        return self.serial
