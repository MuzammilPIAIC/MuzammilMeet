from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Lobby, name='Lobby'),
    path('room/', Room, name='Room'),
    path('get_token/', getToken, name='gettoken'),
    
]
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)