from django.db import models

# Instruments
class Instrument(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Name")
    repertoire=models.CharField(
        max_length=250,
        verbose_name="Directory",null=True, blank=True)    
    def __str__(self) -> str:
        return f"{self.nom} {self.repertoire}"
    
# Styles de musiques
class Style(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Nom du style")
    
    def __str__(self) -> str:
        return f"{self.nom}"
    
# Morceaux
class Morceau(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Nom du morceau")
    duree=models.CharField(
        max_length=5,
        verbose_name="Durée du morceau",
        null=True, blank=True)
    date_debut=models.DateField(null=True, blank=True)
    date_fin=models.DateField(null=True, blank=True)
    commentaire=models.TextField(null=True, blank=True)
    locked=models.BooleanField(default=False)
    termine=models.BooleanField(default=False)
    mixe=models.BooleanField(default=False)
    documentation=models.BooleanField(default=False)
    fichier_documentation=models.CharField(
        max_length=255,
        null=True, blank=True)
    support=models.CharField(
        max_length=20,
        null=True, blank=True)
    work_directory=models.CharField(
        max_length=255,
        null=True, blank=True)
    liste_instruments=models.ForeignKey(Instrument,on_delete=models.CASCADE)
    type=models.CharField(
        max_length=30,
        null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nom} {self.duree} - {self.date_fin}"
