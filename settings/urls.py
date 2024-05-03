from django.urls import path
from settings.views import settings_import
from settings import views

urlpatterns = [
    path('import.html',settings_import),
    #path('import_exec', views.import_exec,name="import_exec"),
    # Ajoutez d'autres URLs si nécessaire
]