from django.views.generic import TemplateView
from . import models

class Home(TemplateView):
    template_name = "main.html"

    
