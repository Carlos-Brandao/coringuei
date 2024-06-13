from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def eventos(request):
    return render(request,'events.html')
    
def inscrito(request):
    return render(request,'event-detail.html')
   
def evento_detalhe(request):
    return render(request, 'event-detail.html')     

