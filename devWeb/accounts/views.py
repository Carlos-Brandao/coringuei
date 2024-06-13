from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_login(request):
    return render(request,'login2.html')
    
def registro(request):
    return render(request,'register2.html')
        