from django.http import HttpResponse
from django.shortcuts import render

from morceaux.models import Morceau

# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        context= {"morceaux": Morceau.objects.all()}
    else:
        context= {}

    return render(request, template_name="website/welcome.html", context=context)

#def index(request):
#    return HttpResponse("ARTSEN - Gestion des compositions")

def index(request):
    return render(request, template_name="website/index.html")

def about(request):
    nb_compositions=Morceau.objects.count()
    return render(request, template_name="website/welcome.html",context={"nb_compositions":nb_compositions})
