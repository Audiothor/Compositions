from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from morceaux.models import Instrument,Morceau
import os
import shutil
from datetime import datetime

class DFichier:
    def __init__(self, name_f, extension_f,date_f):
        self.name_f = name_f
        self.extension_f = extension_f
        self.date_f = date_f

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
            files_list=select_files_details(directories,daw_import)
            if not files_list:
                instruments=Instrument.objects.all()
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': 'No standard files found !'})
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
                        print(song_nom+" locked !!!")
                        break
                    else:
                        print(song_nom+" not locked !!!")
                        song_date_debut,song_date_fin=oldest_newest_file(directory,".song")
                        #b=Morceau(id=request['id'],date_debut=song_date_debut,date_fin=song_date_fin)
                        id=request[0]['id']
                        work_file=get_mixdown(directory,song_nom)
                        Morceau.objects.filter(pk=id).update(date_debut=song_date_debut,work_directory=work_file,date_fin=song_date_fin)
                        #b.save()
                else:
                    print("Have to create !!")
                    # create
                    song_date_debut,song_date_fin=oldest_newest_file(directory,".song")
                    #mixdown=import_mixdown(directory)
                    if not song_date_debut:
                        break
                    # Default values :
                    song_liste_instruments=daw_id
                    song_locked=True
                    song_work_directory=directory
                    song_type=""
                    song_documentation=False
                    song_fichier_documentation=""
                    song_mixe=False
                    song_termine=False
                    song_commentaire=""
                    song_duree="3:00"
                    song_support="1"
                    song_duree="3:00"
                    song_support="1"
                    b = Morceau(nom=song_nom, date_debut=song_date_debut,date_fin=song_date_fin,liste_instruments=song_liste_instruments,locked=song_locked,work_directory=song_work_directory,type=song_type,documentation=song_documentation,fichier_documentation=song_fichier_documentation,mixe=song_mixe,termine=song_termine,commentaire=song_commentaire,duree=song_duree,support=song_support)
                    b.save()

        #1 name
        # Ableton le mixdown est contenu dans ....
        # Studio One dans mixdown
        

    return ([])

def get_mixdown(directory,song_nom):
    mixdown_dir=directory+"/Mixdown"
    if os.path.isdir(mixdown_dir):
        tous_fichiers = os.listdir(mixdown_dir)
        suffixes = (".wav",".WAV",".mp3",".MP3")
        fichiers_song = [os.path.join(mixdown_dir, file) for file in tous_fichiers if file.endswith(suffixes)]
        fichiers_tries = sorted(fichiers_song, key=os.path.getctime)
        # More recent
        fichier_work=os.path.basename(fichiers_tries[-1])
        extension=os.path.splitext(fichier_work)
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
    # Utilisez os.listdir pour obtenir une liste de tous les fichiers dans le répertoire
    tous_fichiers = os.listdir(directory)

    # Filtrer les fichiers par extension.song
    fichiers_song = [os.path.join(directory, file) for file in tous_fichiers if file.endswith(extension)]
    # Tri des fichiers par date de création du plus ancien au plus récent
    fichiers_tries = sorted(fichiers_song, key=os.path.getctime)
    # Afficher les fichiers triés
    # for fichier in fichiers_tries:
    #     print(fichier)

    oldest = os.path.getctime(fichiers_tries[0])
    newest = os.path.getctime(fichiers_tries[-1])

    dt_object = datetime.fromtimestamp(oldest)
    old = dt_object.strftime('%Y-%m-%d')
    dt_object = datetime.fromtimestamp(newest)
    new = dt_object.strftime('%Y-%m-%d')

    # stats = os.stat(str(oldest))
    # creation_time = stats.st_birthtime
    # print(creation_time)

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