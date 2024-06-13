from django.urls import path
from . import views
urlpatterns = [
    path('', views.verTrabalho, name ="verTrabalho" ),
    
]
