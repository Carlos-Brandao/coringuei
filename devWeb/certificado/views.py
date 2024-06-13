from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def certificado(request):
    return render(request,'certificados.html')
