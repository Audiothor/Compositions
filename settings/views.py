from django.http import HttpResponse
from django.shortcuts import render

def settings_import(request):
    # Traitement de la requête si nécessaire
    context = {
        'variable': 'valeur',  # Ajoutez des variables de contexte si nécessaire
    }
    return render(request, template_name="settings/import.html", context=context)