from django.http import HttpResponse
from django.shortcuts import render

from morceaux.models import Morceau
from news.models import News

from settings.forms import Config
from django.conf import settings

import yaml
##########################################################################
# Load de Config YAML file
def load_config():
        config_file = settings.STATICFILES_DIRS[0]+'config/compositions.yaml'
        form = Config()
        # Open the YAML file and load its data
        with open(config_file, 'r') as file:
            donnees_yaml = yaml.safe_load(file)
        form = Config(initial=donnees_yaml)

        return form
##########################################################################

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
    # morceaux
    nb_compositions=Morceau.objects.count()
    morceaux=Morceau.objects.all().order_by('-date_fin')[:5]

    # Load the config file
    config_form=load_config()
    # Sort the news
    news_print_sorted_creation_date = config_form['news_print_sorted_creation_date'].value()
    if news_print_sorted_creation_date:
        order_by = '-date_creation'
    else:
        order_by = 'order'
    news=News.objects.all().order_by(order_by)

    return render(request, template_name="website/index.html",context={"news": news,"morceaux": morceaux,"nb_compositions":nb_compositions,"config_form":config_form})

#    return render(request, template_name="website/index.html",context = {
#        'ALERT_CLASS': 'alert-success',
#        'ALERT_TYPE': 'SUCCESS',
#        'ALERT_MESSAGE': 'Hello, World!',
#        # Add more variables as needed
#    })

def biography(request):

    config_form=load_config()

    return render(request, template_name="website/biography.html",context={"config_form":config_form})

def about(request):
    nb_compositions=Morceau.objects.count()
    return render(request, template_name="website/welcome.html",context={"nb_compositions":nb_compositions})
