from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.ver_login, name ="verlogin" ),
    path('register/', views.registro, name ="registro" ),
]
