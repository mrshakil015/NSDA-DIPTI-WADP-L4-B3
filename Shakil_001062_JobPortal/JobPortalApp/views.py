from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def registrationPage(request):
    if request.method == 'POST':
        pass
    else:
        pass
        

    return render(request,'signup.html')

def loginPage(request):
    
    
    return render(request,'')
