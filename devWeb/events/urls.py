from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path('', views.eventos, name ="verEventos" ),
    path('inscrito/', views.inscrito, name ="pagina registro" ),
    path('evento1/', views.evento_detalhe, name ="eventoDetalhe" ),
    
]
