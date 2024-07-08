from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def registrationPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        displayname = request.POST.get('displayname')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = JobPortalUser.objects.create_user(
                username = username,
                DisplayName=displayname,
                email=email,
                UserType=usertype,
                password = password, 
            )
            user.save()
            if usertype == 'Recruiters':
                recrcreate = RecruitersModel.objects.create(jobuser = user)
                recrcreate.save()
            else:
                seekercreate = RecruitersModel.objects.create(jobuser = user)
                seekercreate.save()
            return redirect('loginPage')
    
    return render(request,'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('profile')
    return render(request,'signin.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def profile(request):
    
    return render(request,'profile.html')

@login_required
def addjob(request):
    current_user = request.user
    if request.method == 'POST':
        jobform = JobForm(request.POST)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.Created_By = current_user
            job.save()
            return redirect('browsejob')
    else:
        jobform = JobForm()
    context = {
        'jobform':jobform,
    }
    return render(request,'addjob.html',context)

def browsejob(request):
    
    
    return render(request, 'browsejob.html')