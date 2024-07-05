from django.urls import path, include
from rest_framework import routers
from .views import UsuarioView
router = routers.DefaultRouter()
router.register(r'usuario', UsuarioView)

urlpatterns = [
    path('', include(router.urls))
]
