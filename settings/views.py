# settings/views.py
###################
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import yaml
import sqlite3 
import io 

from morceaux.models import Instrument,Morceau

from settings.forms import Config
import os
import shutil
from django.conf import settings
from datetime import datetime

class DFichier:
    def __init__(self, name_f, extension_f,date_f):
        self.name_f = name_f
        self.extension_f = extension_f
        self.date_f = date_f

@login_required
def config_edit(request):
    config_file = settings.STATICFILES_DIRS[0]+'config/compositions.yaml'

    if request.method == 'POST':
        if 'update' in request.POST:
            form = Config(request.POST)
            if form.is_valid():
                # Ici, vous pouvez également sauvegarder les données dans la base de données si nécessaire
                # form.save()

                # Préparation des données pour le fichier YAML
                donnees_yaml = {
                    'display_website_name': form.cleaned_data['display_website_name'],
                    'news_print_sorted_creation_date': form.cleaned_data['news_print_sorted_creation_date'],
                    'news_print_creation_date': form.cleaned_data['news_print_creation_date'],
                    'news_print_news_type': form.cleaned_data['news_print_news_type'],
                    'news_print_last_five_music': form.cleaned_data['news_print_last_five_music'],
                    'news_print_news': form.cleaned_data['news_print_news'],
                    'news_print_text_welcome': form.cleaned_data['news_print_text_welcome'],
                    'news_print_image_welcome': form.cleaned_data['news_print_image_welcome'],
                    'news_text_input_welcome': form.cleaned_data['news_text_input_welcome'],
                    'news_image_input_welcome': form.cleaned_data['news_image_input_welcome'],
                    'news_print_number_musics_page': form.cleaned_data['news_print_number_musics_page'],
                    'musics_list_view': form.cleaned_data['musics_list_view'],
                    'musics_print_hits': form.cleaned_data['musics_print_hits'],
                }

                # from django.contrib.auth.models import User
                # user = User.objects.get(username='<old_username>')
                # user.username = '<new_username>'
                # user.email = '<new_email>'
                # user.is_staff = True  # Ensure the user has admin privileges

                # user = User.objects.get(username='<username>')
                # user.set_password('<new_password>')
                # user.save()

                # Écriture des données dans le fichier YAML
                with open(config_file, 'w') as fichier:
                    yaml.dump(donnees_yaml, fichier, default_flow_style=False, allow_unicode=True)

                return render(request, 'settings/config.html', context={'form': form,'ALERT_CLASS': 'alert-success','ALERT_TYPE': 'INFO','ALERT_MESSAGE': 'Config file save done !'})           # Vous pouvez rediriger l'utilisateur ou afficher un message de succès ici

        if 'backup' in request.POST:
            now = datetime.now()
            timestamp=f"{now.year}{now.month}{now.day}-{now.hour}{now.minute}{now.second}"
            backup_file='saves/backupdatabase_dump_'+timestamp+'.sql'
            message='Backup '+backup_file+' done !'
            conn = sqlite3.connect('db.sqlite3')    
            # Open() function  
            with io.open(backup_file, 'w') as p:           
                # iterdump() function 
                for line in conn.iterdump():           
                    p.write('%s\n' % line)         
            print(' Backup performed successfully!') 
            print(' Data Saved as backupdatabase_dump.sql')    
            conn.close()
            form = Config()
            return render(request, 'settings/config.html', context={'form': form,'ALERT_CLASS': 'alert-success','ALERT_TYPE': 'INFO','ALERT_MESSAGE': message})           # Vous pouvez rediriger l'utilisateur ou afficher un message de succès ici

        form = Config()
        # Open the YAML file and load its data
        with open(config_file, 'r') as file:
            donnees_yaml = yaml.safe_load(file)
            form = Config(initial=donnees_yaml)
        return render(request, 'settings/config.html', {'form': form})
    else:
        form = Config()
        # Open the YAML file and load its data
        with open(config_file, 'r') as file:
            donnees_yaml = yaml.safe_load(file)
        form = Config(initial=donnees_yaml)

        return render(request, 'settings/config.html', {'form': form})


@login_required
def settings_import(request):
    if request.method=="POST":

        daw=request.POST.getlist("chk")
        daw_import=request.POST.get("daw_import")
        directories=request.POST.getlist("chk_directories")
        #print(directories)
        #print(daw)

        if not daw and not directories:
            #print("vide")
            # Traitement de la requête si nécessaire
            instruments=Instrument.objects.all()
            return render(request, template_name="settings/import.html",context={"instruments":instruments})
        
        if daw:
            directories_list=select_directories(daw)
            #print(daw)
            # Error : no data
            if not directories_list:
                instruments=Instrument.objects.all()
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': 'No directories found to analyze !'})
            else:
                #print(directories_list)
                dawtab = daw[0].split(";")
                daw_id = dawtab[0]
                daw_name = dawtab[1]
                #print(daw_name)
                return render(request,"settings/import_select.html",context={'directories_list':directories_list,'daw':daw,'daw_name':daw_name,'daw_id':daw_id})
        
        if directories:
            message_type,message_text=select_files_details(directories,daw_import)
            print(message_text)
            instruments=Instrument.objects.all()
            if message_type == "ERROR":
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': message_text})
            if message_type == "SUCCESS":
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-success','ALERT_TYPE': 'SUCCESS','ALERT_MESSAGE': message_text})
    else:
        # Traitement de la requête si nécessaire
        instruments=Instrument.objects.all()
        return render(request, template_name="settings/import.html",context={"instruments":instruments})


def select_directories(daw):
    dawtab = daw[0].split(";")
    daw_id=dawtab[0]
    daw_name = dawtab[1]
    daw_directory = dawtab[2]

    #print("Name=",daw_name)
    #print("Directory=",daw_directory)

    if (os.path.exists(daw_directory)):
        max_depth = 2
        directories_list = list_dir_recursive(daw_directory, depth=max_depth)
    else:
        #print("Directory:",daw_directory,"not exists...")
        directories_list=[]
    return directories_list

def select_files_details(directories,daw_import):
    #print(directories)
    # 0. Extract name of the instrument used
    # 1. Extract name of the composition
    # 2. Extract the oldest file created to identify the start of the project
    # 3. Extract date of the mixdown to identify the end of the project
    # 4. Extract the duration of the music
    dawtab = daw_import.split(";")
    daw_id=dawtab[0]
    daw_name=dawtab[1]
    message_type=""
    message_text="-"

    for directory in directories:
        print("Directory:"+directory)
        # O instrument
        # Tableau de de fichier type DFichier
        version=[]
        #inst=Instrument.objects.filter(repertoire__contains='fsenella').values()
        insts=Instrument.objects.all()
        match str(daw_name):
            case str("Ableton Live"):
                print("Ableton Live")
            case str("Studio One"):
                print("Studio One")

                song_nom=os.path.basename(directory)
                # Check if exist
                request=work_exists(song_nom)
                if request:
                    if work_locked(song_nom):
                        message_type="ERROR"
                        message_text="This work is locked !"
                        break
                    else:
                        print(song_nom+" not locked !!!")
                        song_date_debut,song_date_fin=oldest_newest_file(directory,".song")
                        id=request[0]['id']
                        #print("id=",id)
                        b=Morceau.objects.get(id=int(id))
                        #print(b)
                        work_file=get_mixdown(directory,song_nom)
                        print("work_file=",work_file)
                        #Morceau.objects.filter(pk=id).update(date_debut=song_date_debut,work_directory=work_file,date_fin=song_date_fin)
                        b.date_debut=song_date_debut
                        b.date_fin=song_date_fin
                        b.music_file=work_file
                        b.save()
                        message_type="SUCCESS"
                        message_text="Update "+b.nom+" done !"
                else:
                    print("Have to create !!")
                    # create
                    print("1")
                    song_date_debut,song_date_fin=oldest_newest_file(directory,".song")
                    print("1.5")
                    if song_date_debut is None:
                        message_type="ERROR"
                        message_text="Update No extension file .song found !"
                        break
                    #mixdown=import_mixdown(directory)
                    if not song_date_debut:
                        break
                    # Default values :
                    song_liste_instruments=daw_id
                    print(song_liste_instruments)
                    song_locked=True
                    song_work_directory=directory
                    song_style=""
                    song_documentation=False
                    song_fichier_documentation=""
                    song_mixed=False
                    song_finished=False
                    song_commentaire=""
                    song_duree="3:00"
                    song_support="1"
                    song_duree="3:00"
                    song_support="1"
                    b = Morceau(nom=song_nom, date_debut=song_date_debut,date_fin=song_date_fin,instrument_id=song_liste_instruments,locked=song_locked,work_directory=song_work_directory,style_id=song_style,documentation=song_documentation,fichier_documentation=song_fichier_documentation,mixed=song_mixed,finished=song_finished,commentaire=song_commentaire,duree=song_duree,support=song_support)
                    b.save()
                    message_type="SUCCESS"
                    message_text="Creation new work : "+song_nom+" done !"

        #1 name
        # Ableton le mixdown est contenu dans ....
        # Studio One dans mixdown
        

    #return ([])
    return message_type,message_text

def get_mixdown(directory,song_nom):
    mixdown_dir=directory+"/Mixdown"
    if os.path.isdir(mixdown_dir):
        tous_fichiers = os.listdir(mixdown_dir)
        suffixes = (".wav",".WAV",".mp3",".MP3")
        fichiers_song = [os.path.join(mixdown_dir, file) for file in tous_fichiers if file.endswith(suffixes)]
        fichiers_tries = sorted(fichiers_song, key=os.path.getctime)
        # More recent
        fichier_work=os.path.basename(fichiers_tries[-1])
        print(fichier_work)
        extension=os.path.splitext(fichier_work)
        print(extension)
        fichier_final=song_nom.replace(" ", "_")+extension[1]
        fichier_target="/home/fsenella/compositions/static"+"/musics/"+fichier_final
        shutil.copyfile(mixdown_dir+"/"+fichier_work,fichier_target) 
        return fichier_final        
    else:
        return ""
    

def work_exists(work_name):
    morceaux = Morceau.objects.filter(nom__contains=work_name).values()
    if not morceaux:
        return None
    else:
        return morceaux


def work_locked(work_name):
    morceaux = Morceau.objects.filter(nom__contains=work_name).values()
    result=morceaux.filter(locked__exact=True)
    if not result:
        return False
    else:
        return True
    
def oldest_newest_file(directory,extension):
    print(directory)
    print(extension)
    # Utilisez os.listdir pour obtenir une liste de tous les fichiers dans le répertoire
    tous_fichiers = os.listdir(directory)

    # Filtrer les fichiers par extension.song
    fichiers_song = [os.path.join(directory, file) for file in tous_fichiers if file.endswith(extension)]
    if not fichiers_song:
        return None,None
    
    # Tri des fichiers par date de création du plus ancien au plus récent
    fichiers_tries = sorted(fichiers_song, key=os.path.getctime)
    # Afficher les fichiers triés
    # for fichier in fichiers_tries:
    #     print(fichier)
    print(fichiers_tries)

    oldest = os.path.getctime(fichiers_tries[0])
    newest = os.path.getctime(fichiers_tries[-1])

    dt_object = datetime.fromtimestamp(oldest)
    old = dt_object.strftime('%Y-%m-%d')
    dt_object = datetime.fromtimestamp(newest)
    new = dt_object.strftime('%Y-%m-%d')

    # stats = os.stat(str(oldest))
    # creation_time = stats.st_birthtime
    # print(creation_time)
    print("old=",old,"new=",new)
    return old,new

# result=array of the result
# resultd=the directory name and the depth
def list_dir_recursive(directory, depth=None, current_depth=0, result=None,resultd=None):
    if result is None:
        result = []
    if depth is not None and current_depth >= depth:
        return result
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            #print("full_path",full_path,"current_depth",current_depth)
            resultd = ['','']
            resultd[0]=full_path
            resultd[1]=str(current_depth)
            result.append(resultd)
            list_dir_recursive(full_path, depth, current_depth + 1, result,resultd=None)
    return result,resultd


# @login_required
# def settings_import(request):
#     # Traitement de la requête si nécessaire
#     context = {
#         'variable': 'valeur',  # Ajoutez des variables de contexte si nécessaire
#     }
#     return render(request, template_name="settings/import.html", context=context)