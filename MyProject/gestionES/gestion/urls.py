from django.urls import path
from .import views

app_name = 'gestion'
urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    #path('ventes/', views.ventes_mois_dernier, name='ventes_mois_dernier'),
]
