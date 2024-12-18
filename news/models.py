from django.db import models
from datetime import date

# Instruments
class News(models.Model):
    title=models.CharField(
        max_length=150,
        verbose_name="Name")
    LIST_TYPE = (("",""),("New music","New music"),("Information","Information"),("Concert","Concert"))
    type=models.CharField(max_length=50, choices=LIST_TYPE)
    morceau=models.ForeignKey('morceaux.Morceau',on_delete=models.CASCADE,blank=True, null=True)
    comment=models.TextField(blank=True)
    order=models.IntegerField(blank=True,default=1)
    date_creation=models.DateField(default=date.today,null=True, blank=True)
    start_publication=models.DateField(default=date.today,null=True, blank=True)
    end_publication=models.DateField(default=date.today,null=True, blank=True)
    activated=models.BooleanField(default=True)
    class Meta:
        ordering = ['date_creation']

    def __str__(self) -> str:
        return f"{self.title}"
