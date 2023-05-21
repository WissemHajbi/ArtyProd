from django.urls import path
from .views import Home, Login, Register, Logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', Home, name="home"),
    path('login', Login, name="login"),
    path('register', Register, name="register"),
    path('logout', Logout, name="logout")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)