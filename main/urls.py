from django.urls import path
from .views import Home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', Home.as_view(), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)