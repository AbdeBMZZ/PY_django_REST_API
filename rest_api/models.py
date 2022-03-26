from django.db import models

# Create your models here.


class Etudiant(models.Model):
    cne = models.CharField(max_length=20)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)

    def __str__(self):
        return f"cne: {self.cne}, nom: {self.nom}, prenom: {self.prenom}"
