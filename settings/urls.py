from django.urls import path
from settings.views import settings_import,config_edit
from settings import views

urlpatterns = [
    path('import.html',settings_import),
    path('config.html',config_edit),
    #path('import_exec', views.import_exec,name="import_exec"),
    # Ajoutez d'autres URLs si nécessaire
]