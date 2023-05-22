from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()

    def str(self):
        return self.type

class Detail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    fichier = models.FileField(upload_to='uploads/')

    def str(self):
        return self.fichier.name

class Project(models.Model):
    equipe = models.OneToOneField('Equipe', on_delete=models.SET_NULL, null=True, blank=True, related_name='project')
    libellai = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    photo = models.ImageField(default="")

    def str(self):
        return self.libellai

class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    personnel = models.ManyToManyField('Personnel')

    def str(self):
        return self.nom

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField()
    photo = models.ImageField()
    lien_linkedIn = models.URLField(blank=True)

    def str(self):
        return self.user.username

    