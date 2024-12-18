from django.db import models

# Instruments
class Instrument(models.Model):
    nom=models.CharField(
        max_length=150,
        verbose_name="Name")
    repertoire=models.CharField(
        max_length=250,
        verbose_name="Directory",null=True, blank=True)
    
    class Meta:
        ordering = ['nom']

    def __str__(self) -> str:
        return f"{self.nom}"
    
# Genre de musiques
class Style(models.Model):
    nom=models.CharField(
        max_length=200,
        verbose_name="Style")
    
    def __str__(self) -> str:
        return f"{self.nom}"
    
# Morceaux
class Morceau(models.Model):
    nom=models.CharField(
        max_length=150,
        verbose_name="Nom du morceau",null=True, blank=True)
    duree=models.CharField(
        max_length=8,
        verbose_name="Durée du morceau",
        null=True, blank=True)
    date_debut=models.DateField(null=True, blank=True)
    date_fin=models.DateField(null=True, blank=True)
    commentaire=models.TextField(null=True, blank=True)
    locked=models.BooleanField(default=False)
    finished=models.BooleanField(default=False)
    mixed=models.BooleanField(default=False)
    documentation=models.BooleanField(default=False)
    fichier_documentation=models.CharField(
        max_length=255,
        null=True, blank=True)
    hits=models.IntegerField(default=0)
    support=models.CharField(
        max_length=20,
        null=True, blank=True)
    instrument=models.ManyToManyField(Instrument)
    style=models.ManyToManyField(Style)

    download=models.BooleanField(default=True)
    player=models.BooleanField(default=True)
    music_file = models.FileField(upload_to="musics",null=True,blank=True)
    image_file = models.FileField(upload_to="images",null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.nom}"
