from django.contrib import admin
from django.contrib.admin import ModelAdmin

from morceaux.models import Morceau,Instrument,Style

# Register your models here.
@admin.register(Morceau)
class MorceauAdmin(ModelAdmin):
    model = Morceau
    list_display=("id","nom","date_debut","date_fin","termine")
    ordering=("date_debut","date_fin","nom")
    search_fields=("nom",)

# Class Instrument : Faire apparaitre dans le Django administration
admin.site.register(Instrument)

# Class Style : Faire apparaitre dans le Django administration
admin.site.register(Style)