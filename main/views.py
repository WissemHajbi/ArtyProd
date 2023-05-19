from django.views.generic import TemplateView
from . import models

class Home(TemplateView):
    template_name = "main.html"
    model = models.Project
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = models.Project.objects.all()
        context["services"] = models.Service.objects.all()
        context["personnel"] = models.Personnel.objects.all()
        
        return context
    