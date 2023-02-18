from django.contrib import admin

# Register your models here.

from gestion.models import Produit , Fournisseur , Client , Bon_Commande , Bon_Livraison


admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Bon_Commande)
admin.site.register(Bon_Livraison)
