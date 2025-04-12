from webbrowser import register

from django.urls import path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router = register(r'', ProductViewSets, basename='products' )
router = register(r'', ProductViewSets, basename='products' )



urlpatterns = [
