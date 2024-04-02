from django.db import models


class Instrument(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Nom de l'instrument")
    
    def __str__(self) -> str:
        return f"{self.nom}"
    

class Morceau(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Nom du morceau")
    duree=models.CharField(
        max_length=5,
        verbose_name="Durée du morceau",
        default="")
    date_debut=models.DateField()
    date_fin=models.DateField()
    commentaire=models.TextField(
        default="")
    termine=models.BooleanField(default=False)
    mixe=models.BooleanField(default=False)
    documentation=models.BooleanField()
    fichier_documentation=models.CharField(
        max_length=255,
        default="")
    support=models.CharField(
        max_length=20,
        default="")
    liste_instruments=models.ForeignKey(Instrument,on_delete=models.CASCADE)
    type=models.CharField(
        max_length=30,
        default="")
    
    def __str__(self) -> str:
        return f"{self.nom} {self.duree} - {self.date_fin}"
