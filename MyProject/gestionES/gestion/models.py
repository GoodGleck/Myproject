from django.db import models

# Create your models here.


class Fournisseur(models.Model):
    NomFour = models.CharField(max_length=100)
    AdrFour = models.CharField(max_length=200)
    TelFour = models.CharField(max_length=20)

    def __str__(self):
        return self.NomFour

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=[('B', 'Brut'), ('F', 'Fin')])
    quantite = models.IntegerField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Client(models.Model):
    NomClient = models.CharField(max_length=100)
    AdrClient = models.CharField(max_length=200)
    TelClient = models.CharField(max_length=20)

    def __str__(self):
        return self.NomClient

class Bon_Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=[('I', 'Entrée'), ('E', 'Sortie')])
    quantite = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.produit

class Bon_Livraison(models.Model):
    commande = models.ForeignKey(Bon_Commande, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=[('I', 'Entrée'), ('E', 'Sortie')])
    quantite = models.IntegerField()
    date = models.DateField()

