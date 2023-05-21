from django import forms
from django.forms import ModelForm
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class ProduitForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"  

# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"  


# class FournisseurForm(ModelForm):
#     class Meta:
#         model = Fournisseur
#         fields = "__all__" 


# class CommandeForm(forms.ModelForm):
#     class Meta:
#         model = Commande
#         fields = ['dateCde', 'nom_client',
#                   'adresse_livraison', 'produits', 'totalCde']
#         widgets = {
#             'produits': forms.CheckboxSelectMultiple()
#         }


# class CategorieForm(ModelForm):
#     class Meta:
#         model = Categorie
#         fields = "__all__" 


# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(label='Prénom')
#     last_name = forms.CharField(label='Nom')
#     email = forms.EmailField(label='Adresse e-mail')

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + \
#             ('first_name', 'last_name', 'email')
