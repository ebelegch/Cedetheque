from django.db import models

# Create your models here.
class musique(models.Model):
    nom_album = models.CharField(max_length=300)
    num_piste = models.CharField(max_length=1)
    titre = models.CharField(max_length=300)
    auteur  = models.CharField(max_length=300)
    compositeur  = models.CharField(max_length=300)
    interprete = models.CharField(max_length=300)
   # pochette = models.
    pub_date = models.DateTimeField('date published')
