from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator # Create your models here
class Ikasle(models.Model): 
    id = models.AutoField(primary_key=True)    
    izena = models.CharField(max_length=75)    
    abizena = models.CharField(max_length=100)    
    jaiotze_data = models.DateTimeField(default=timezone.now)    
    def __str__(self):       
        return f"Ikaslearen izena {self.izena} da eta abizena {self.abizena}."
class Ikasgaiak(models.Model): 
    id = models.AutoField(primary_key=True) 
    izena = models.CharField(max_length=75)
    maila = models.CharField(max_length=75) 
    hizkuntza = models.CharField(max_length=75)           

    def __str__(self):
        return f"Ikasgaia {self.izena}  {self.maila} {self.hizkuntza}."
class Nota(models.Model): 
    nota = models.BigIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),  # Mínimo valor de 0
            MaxValueValidator(10)  # Máximo valor de 10
        ]
    )
    oharra = models.CharField(max_length=75)
    ikasgai_kodea = models.ForeignKey(Ikasgaiak,on_delete=models.CASCADE) 
    ikasle_kodea =models.ForeignKey(Ikasle, on_delete=models.CASCADE)        

    def __str__(self):
        return f"{self.ikasle_kodea.izena}{self.ikasle_kodea.abizena} ikasleak {self.nota} bat atera du {self.ikasgai_kodea.izena} ikasgaian ohar honekin:{self.oharra}."    


# Create your models here.
