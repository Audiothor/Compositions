from django.contrib import admin
from django.contrib.admin import ModelAdmin

from morceaux.models import Morceau,Instrument

# Register your models here.
@admin.register(Morceau)
class MorceauAdmin(ModelAdmin):
    model = Morceau
    list_display=("id","nom","date_debut","date_fin","termine")
    ordering=("date_debut","date_fin","nom")
    search_fields=("nom",)

admin.site.register(Instrument)