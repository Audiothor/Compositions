from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from morceaux.models import Instrument,Morceau
import os

@login_required
def settings_import(request):
    if request.method=="POST":

        daw=request.POST.getlist("chk")
        directories=request.POST.getlist("chk_directories")
        print(directories)

        if not daw and not directories:
            #print("vide")
            # Traitement de la requête si nécessaire
            instruments=Instrument.objects.all()
            return render(request, template_name="settings/import.html",context={"instruments":instruments})
        
        if daw:
            directories_list=select_directories(daw)
            # Error : no data
            if not directories_list:
                instruments=Instrument.objects.all()
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': 'No directories found to analyze !'})
            else:
                print(directories_list)
                return render(request,"settings/import_select.html",{'directories_list':directories_list})
        
        if directories:
            files_list=select_files_details(directories)
            if not files_list:
                instruments=Instrument.objects.all()
                return render(request,"settings/import.html",context={"instruments":instruments,'ALERT_CLASS': 'alert-danger','ALERT_TYPE': 'ERROR','ALERT_MESSAGE': 'No standard files found !'})
    else:
        # Traitement de la requête si nécessaire
        instruments=Instrument.objects.all()
        return render(request, template_name="settings/import.html",context={"instruments":instruments})


def select_directories(daw):
    print(daw)
    dawtab = daw[0].split(";")
    daw_name = dawtab[0]
    daw_directory = dawtab[1]

    #print("Name=",daw_name)
    #print("Directory=",daw_directory)

    if (os.path.exists(daw_directory)):
        max_depth = 2
        directories_list = list_dir_recursive(daw_directory, depth=max_depth)
    else:
        #print("Directory:",daw_directory,"not exists...")
        directories_list=[]
    return directories_list

def select_files_details(directories):
    print(directories)

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