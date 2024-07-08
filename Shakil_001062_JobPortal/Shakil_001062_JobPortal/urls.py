from django.contrib import admin
from django.urls import path
from JobPortalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage,name="loginPage"),
    path('registrationPage/',registrationPage,name="registrationPage"),
    path('profile/',profile,name="profile"),
    path('addjob/',addjob,name="addjob"),
    path('browsejob/',browsejob,name="browsejob"),
    path('logoutpage/',logoutpage,name="logoutpage"),
    
]
