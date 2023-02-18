from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta



#Mes imports du models
from .models import Produit , Bon_Livraison

def liste_produits(request):
    produits = Produit.objects.filter(type='B', quantite__gt=0)
    return render(request, 'gestion/liste_produits.html', {'produits': produits})




"""def ventes_mois_dernier(request):

    date_debut = timezone.localtime().replace(day=1) - timezone.timedelta(days=1)

    #date_debut = date.today().replace(day=1) - timedelta(days=1)
    date_fin = date_debut.replace(day=1)
    ventes = Bon_Livraison.objects.filter(
        type='I',
        date__range=(date_fin, date_debut)
    ).values('produit').annotate(total=Sum('quantite'))
    return render(request, 'gestion/ventes.html', {'ventes': ventes})
    """