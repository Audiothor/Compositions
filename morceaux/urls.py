from django.urls import path
from morceaux import views

urlpatterns = [
    path('<int:id>', views.detail,name="detail"),
    path('',views.morceaux_list,name="morceaux"),
    path('styles/',views.styles_list,name="styles_list"),
    path('style_new',views.style_new,name="style_new"),
    path('style_edit/<int:id>',views.style_edit,name="style_edit"),
    path('style_delete/<int:id>',views.style_delete,name="style_delete"),
    path('morceau_nouveau',views.morceau_nouveau,name="morceau_editer"),
    path('morceau_editer/<int:id>',views.morceau_editer,name="morceau_editer"),
    path('morceau_cloner/<int:id>',views.morceau_cloner,name="morceau_cloner"),
    path('morceau_supprimer/<int:id>',views.morceau_supprimer,name="morceau_supprimer"),
    path('morceau_lock/<int:id>',views.morceau_editer,name="morceau_lock"),
    path('morceau_unlock/<int:id>',views.morceau_editer,name="morceau_unlock"),
    path('morceau_upload',views.morceau_upload,name="morceau_upload"),
    path('export_csv',views.export_csv,name="export_csv"),
    path('search/', views.search_morceau, name='blog-search-post'),
    path('instruments/',views.instruments_list,name="instruments_list"),
    path('instrument_new',views.instrument_new,name="instrument_new"),
    path('instrument_edit/<int:id>',views.instrument_edit,name="instrument_edit"),
    path('instrument_delete/<int:id>',views.instrument_delete,name="instrument_delete"),
]
