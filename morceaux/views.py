# morceaux/views.py
###################
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.forms import modelform_factory

from morceaux.models import Morceau,Instrument,Style
from morceaux.forms import EditerMorceau,EditerInstrument,EditerStyle
from settings.forms import Config

from django.conf import settings

from pydub import AudioSegment
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
# Instruments
InstrumentForm = modelform_factory(Instrument,exclude=[])
@login_required
def instruments_list(request):
    instruments=Instrument.objects.all()

    return render(request, template_name="morceaux/instruments_list.html",context={"instruments":instruments})

@login_required
def instrument_edit(request, id):
    instrument=get_object_or_404(Instrument,pk=id)
    if request.method == "POST":
        form=EditerInstrument(request.POST)
        if form.is_valid():
            instrument.nom = form.cleaned_data['nom']
            instrument.repertoire = form.cleaned_data['repertoire']
            instrument.save()
            return redirect("instruments_list")
    else:
        form = EditerInstrument(initial={'nom': instrument.nom,
                                  'repertoire': instrument.repertoire})
        action_label="Edit"

    return render(request,template_name="morceaux/instrument_edit.html",context={"form": form,"action_label": action_label})


@login_required
def instrument_new(request):
    if request.method == "POST":
        form=InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("instruments_list")
    else:       
        form=InstrumentForm()
        action_label="New"
    return render(request, template_name="morceaux/instrument_edit.html", context={"form": form,"action_label": action_label})


@login_required
def instrument_delete(request, id):
    instrument=get_object_or_404(Instrument,pk=id)
    if request.method == "POST":
        instrument.delete()
        return redirect("instruments_list")
    else:
        return render(request,template_name="morceaux/instrument_confirm_delete.html",context={"instrument": instrument})

############################################################################
# Styles
StyleForm = modelform_factory(Style,exclude=[])
@login_required
def styles_list(request):
    styles=Style.objects.all()
    return render(request, template_name="morceaux/styles_list.html",context={"styles":styles})

@login_required
def style_edit(request, id):
    style=get_object_or_404(Style,pk=id)
    if request.method == "POST":
        form=EditerStyle(request.POST)
        if form.is_valid():
            style.nom = form.cleaned_data['nom']
            style.save()
            return redirect("styles_list")
    else:
        form = EditerStyle(initial={'nom': style.nom})
        action_label="Edit"

    return render(request,template_name="morceaux/style_edit.html",context={"form": form,"action_label": action_label})

@login_required
def style_new(request):
    if request.method == "POST":
        form=StyleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("styles_list")
    else:       
        form=InstrumentForm()
        action_label="New"
    return render(request, template_name="morceaux/style_edit.html", context={"form": form,"action_label": action_label})


@login_required
def style_delete(request, id):
    style=get_object_or_404(Style,pk=id)
    if request.method == "POST":
        style.delete()
        return redirect("styles_list")
    else:
        return render(request,template_name="morceaux/style_confirm_delete.html",context={"style": style})
    
############################################################################
# Morceaux
MorceauForm = modelform_factory(Morceau,exclude=[])
def morceaux_list(request):

    config_form=load_config()

    order_by = request.GET.get('order_by', 'date_fin')
    direction = request.GET.get('direction', 'desc')
    #print(direction)
    if direction == 'desc':
        direction='asc'
    else:
        direction='desc'
        order_by = '-' + order_by
    morceaux = Morceau.objects.all().order_by(order_by)
    #morceaux=Morceau.objects.all()
    total_musics = Morceau.objects.count()
    
    return render(request, template_name="morceaux/morceaux_list.html", context={"morceaux": morceaux,"total_musics": total_musics,"direction":direction,"config_form":config_form})


def detail(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    config_form=load_config()
    return render(request, template_name="morceaux/detail.html",context={"morceau": morceau,"config_form":config_form})


def search_morceau(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        morceaux = Morceau.objects.filter(nom__contains=search_query)
        return render(request, 'morceaux/morceau_search.html', {'query':search_query, 'morceaux': morceaux})
    else:
        return render(request, 'morceaux/morceaux_list.html',{})
    
@login_required
def morceau_nouveau(request):
    Submitted=False
    if request.method == "POST":
        form=MorceauForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:       
        form=MorceauForm()
    return render(request, template_name="morceaux/morceau_nouveau.html", context={"form": form})

@login_required
def morceau_editer(request, id):
    #morceau=get_object_or_404(Morceau,pk=id)
    morceau = Morceau.objects.get(pk=id)
    form = EditerMorceau(request.POST or None, request.FILES or None)

    ImageF=morceau.image_file
    MusicF=morceau.music_file
    reqf=request.FILES
    rfi=reqf.get('image_file')
    rfm=reqf.get('music_file')
    mrf=request.POST.get("music_file-clear")
    irf=request.POST.get("image_file-clear")

    if request.method == "POST":
        if form.is_valid():
            # Update or replace music_file ?
            if rfm is not None:
                print("music change")
                morceau.music_file = form.cleaned_data['music_file']
                duration = get_duration_pydub(morceau.music_file)
                hours, mins, seconds = audio_duration_string(duration)
                morceau.duree="%0.0f:%02d" % (mins,seconds)
            else:
                # Clear music_file ?
                if mrf:
                    morceau.music_file=""
                    morceau.duree=""                 
                else:
                    morceau.music_file = MusicF
                    morceau.duree = form.cleaned_data['duree']


            if rfi is not None:
                morceau.image_file = form.cleaned_data['image_file']
            else:
                # Clear music_file ?
                if irf:
                    morceau.image_file=""              
                else:
                    morceau.image_file = ImageF

            morceau.nom = form.cleaned_data['nom']  
            morceau.date_debut = form.cleaned_data['date_debut']
            morceau.date_fin = form.cleaned_data['date_fin']
            morceau.instrument = form.cleaned_data['instrument']            
            morceau.style = form.cleaned_data['style']
            morceau.locked = form.cleaned_data['locked']
            morceau.mixed = form.cleaned_data['mixed']
            morceau.finished = form.cleaned_data['finished']
            morceau.download = form.cleaned_data['download']
            morceau.player = form.cleaned_data['player']

            morceau.save()

            return redirect("detail", id)
        else:
            print(form.errors)
            return render(request,template_name="morceaux/morceau_editer.html",context={"form": form,"morceau": morceau,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': 'Error in the inputs. Please check the log !'})
    else:
        form = EditerMorceau(initial={'nom': morceau.nom,
                                  'duree': morceau.duree,
                                  'date_debut': morceau.date_debut,
                                  'date_fin': morceau.date_fin,
                                  'locked':morceau.locked,
                                  'instrument':morceau.instrument,
                                  'style':morceau.style,
                                  'mixed':morceau.mixed,
                                  'finished':morceau.finished,
                                  'download':morceau.download,
                                  'player':morceau.player,
                                  'music_file':morceau.music_file,
                                  'image_file':morceau.image_file})

        return render(request,template_name="morceaux/morceau_editer.html",context={"form": form,"morceau": morceau})


@login_required
def morceau_cloner(request, id):
    original_morceau = get_object_or_404(Morceau, pk=id)
    # Get the fields of the model
    fields = [f.name for f in Morceau._meta.fields if f.name != 'id']
    
    # Create a new instance by copying only the relevant fields
    new_morceau_data = {field: getattr(original_morceau, field) for field in fields}
    new_morceau = Morceau(**new_morceau_data)
    
    # Optionally, you can modify some fields here if needed
    # For example, to append "(Copy)" to the title:
    new_morceau.nom += " (Copy)"
    
    # Save the new instance
    new_morceau.save()
    
    # Copy many-to-many relationships
    for field in original_morceau._meta.many_to_many:
        source = getattr(original_morceau, field.name)
        destination = getattr(new_morceau, field.name)
        destination.set(source.all())
    return redirect("morceaux")


@login_required
def morceau_lock(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    if request.method == "POST":
        form = EditerMorceau(request.POST)
        #form=MorceauForm(request.POST, instance=morceau)
        if form.is_valid():
            morceau.locked = form.cleaned_data['locked']
            morceau.save()
            return redirect("detail", id)
    else:
        return render(request, 'morceaux/morceaux_list.html',{})

@login_required
def morceau_supprimer(request, id):
    morceau=get_object_or_404(Morceau,pk=id)
    if request.method == "POST":
        morceau.delete()
        return redirect("morceaux")
    else:
        return render(request,template_name="morceaux/morceau_confirm_delete.html",context={"morceau": morceau})
    
def get_duration_pydub(file_path):
   audio_file = AudioSegment.from_file(file_path)
   duration = audio_file.duration_seconds
   return duration

def audio_duration_string(length): 
    hours = length // 3600  # calculate in hours 
    length %= 3600
    mins = length // 60  # calculate in minutes 
    length %= 60
    seconds = length  # calculate in seconds 
    return hours, mins, seconds  # returns the duration
    