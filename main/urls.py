from django.urls import path
from .views import Home, Login, Register, Logout, Project_details, Demande_project, Edit_project, Delete_project
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', Home, name="home"),
    path('login', Login, name="login"),
    path('logout', Logout, name="logout"),
    path('register', Register, name="register"),
    path('project_details/<int:id>', Project_details, name="project_details"),
    path('demande_project', Demande_project, name="demande_project"),
    path('edit_project/<int:id>', Edit_project, name="edit_project"),
    path('delete_project/<int:id>', Delete_project, name="delete_project"),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)