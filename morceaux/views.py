from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.forms import modelform_factory

from morceaux.models import Morceau,Instrument,Style

def detail(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    return render(request, template_name="morceaux/detail.html",context={"morceau": morceau})

def instruments_list(request):
    instruments=Instrument.objects.all()
    return render(request, template_name="morceaux/instruments_list.html",context={"instruments":instruments})

def styles_list(request):
    styles=Style.objects.all()
    return render(request, template_name="morceaux/styles_list.html",context={"styles":styles})

def morceaux_list(request):
    morceaux=Morceau.objects.all()
    return render(request, template_name="morceaux/morceaux_list.html",context={"morceaux": morceaux})

MorceauForm = modelform_factory(Morceau,exclude=[])

@login_required
def morceau_nouveau(request):
    if request.method == "POST":
        form=MorceauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:       
        form=MorceauForm()
    return render(request, template_name="morceaux/morceau_nouveau.html", context={"form": form})

@login_required
def morceau_editer(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    if request.method == "POST":
        form=MorceauForm(request.POST, instance=morceau)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form=MorceauForm(instance=morceau)
    return render(request,template_name="morceaux/morceau_editer.html",context={"form": form})

@login_required
def morceau_supprimer(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    if request.method == "POST":
        morceau.delete()
        return redirect("index")
    else:
        return render(request,template_name="morceaux/morceau_confirmer_supprimer.html",context={"morceau": morceau})
    