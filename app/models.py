from django.db import models

# Create your models here.

class Urhajos(models.Model):
    
    nev = models.CharField(max_length=255)
    orszag = models.CharField(max_length=255)
    nem = models.CharField(max_length=1)
    szul = models.IntegerField()
    urido = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = "Űrhajós"
        verbose_name_plural = "Űrhajósok"

    def __str__(self):
        return self.nev
    

class Becenev(models.Model):

    nev = models.CharField(max_length=50)
    urhajos = models.ForeignKey(Urhajos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Becenev")
        verbose_name_plural = ("Becenevek")

    def __str__(self):
        return self.name


    




    
   