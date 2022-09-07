from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#from .views import RegisterPage

urlpatterns = [
    path('', views.RegisterPage, name = 'register'),
    path('login/', views.LoginPage, name = 'login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)