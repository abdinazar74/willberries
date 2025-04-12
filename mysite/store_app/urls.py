from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list'}))
]