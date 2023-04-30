# from django.utils import timezone
# from django.db import models

# class Personel(models.Model):
#     nom = models.CharField(max_length=30)
#     fichier_CV = models.CharField(max_length=200)
#     fichier_photo = models.CharField(max_length=200)
#     lien_linkedIn = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.nom


# class Equipe(models.Model):
#     person = models.ForeignKey(
#         user, on_delete=models.CASCADE, related_name='voted_polls')
    
# class Projet(models.Model):
#     libellai = models.CharField(max_length=30)
#     description = models.CharField(max_length=3000)
#     date_debut = models.DateTimeField(default=timezone.now)
#     date_fin = models.DateTimeField(default=timezone.now)
#     acheve = models.BooleanField(default=False)
    
# class Detail(models.Model):
#     fichier = models.CharField(max_length=3000)

# class Service(models.Model):
#     type = models.CharField(max_length=200)
#     description = models.CharField(max_length=3000)
    
# # add the relationships before migrating this to the db
    