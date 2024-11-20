from django.db import models 
from django.utils import timezone
from django.core.validators import MinValueValidator # Create your models here

class Kotxe(models.Model):
    marka = models.CharField(max_length=100)
    modeloa = models.CharField(max_length=100)
    kilometroak = models.IntegerField(validators=[
        MinValueValidator(0)],default=100)
    
    def __str__(self):
        return self.marka
    
class Pertsona(models.Model):
    dni = models.CharField(max_length=50,primary_key=True)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    emaila = models.CharField(max_length=100)
    
    def __str__(self):
        return self.izena
    
class Alokairua(models.Model):
    pertsona = models.ForeignKey(Pertsona,on_delete=models.CASCADE)
    kotxea = models.ForeignKey(Kotxe,on_delete=models.CASCADE)

    alokairu_data_hasi = models.DateField(null=True)
    alokairu_data_bukatu = models.DateField(null=True)