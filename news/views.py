# news/views.py
###################
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.forms import modelform_factory

from news.models import News
from morceaux.models import Morceau
from news.forms import EditNews
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
############################################################################
# News
NewsForm = modelform_factory(News,exclude=[])
@login_required
def news_list(request):
    news=News.objects.all()
    return render(request, template_name="news/news_list.html",context={"news":news})

@login_required
def news_edit(request, id):
    #news=get_object_or_404(News,pk=id)
    news = News.objects.get(pk=id)
    form = EditNews(request.POST)

    print(list(request.POST.items()))
    if request.method == "POST":
        form=EditNews(request.POST)
        if form.is_valid():
            news.title = form.cleaned_data['title']
            news.type = form.cleaned_data['type']
            news.morceau = form.cleaned_data['morceau']
            news.comment = form.cleaned_data['comment']
            news.order = form.cleaned_data['order']
            news.date_creation = form.cleaned_data['date_creation']
            news.start_publication = form.cleaned_data['start_publication']
            news.end_publication = form.cleaned_data['end_publication']
            news.activated = form.cleaned_data['activated']

            news.save()
            return redirect("news")
        else:
            print("edit non valide")
            action_label="Edit"
            print(form.errors)
    else:
        form = EditNews(initial={'title': news.title,
                'type': news.type,
                'morceau': news.morceau,
                'comment': news.comment,
                'order': news.order,
                'date_creation': news.date_creation,
                'start_publication': news.start_publication,
                'end_publication': news.end_publication,
                'activated': news.activated})
        action_label="Edit"
        #print(form)

    return render(request,template_name="news/news_edit.html",context={"form": form,"action_label": action_label,"news": news})


@login_required
def news_add(request):
    if request.method == "POST":
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            print("new non valide")
            action_label="Add"
            print(form.errors)
    else:       
        form=NewsForm()
        action_label="Add"
    return render(request, template_name="news/news_edit.html", context={"form": form,"action_label": action_label})


@login_required
def news_delete(request, id):
    news=get_object_or_404(News,pk=id)
    if request.method == "POST":
        news.delete()
        return redirect("news")
    else:
        return render(request,template_name="news/news_confirm_delete.html",context={"news": news})