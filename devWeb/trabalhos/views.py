from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def verTrabalho(request):
    return render(request,'artigos.html')
    
