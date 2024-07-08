from django.contrib import admin
from django.urls import path
from JobPortalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrationPage/',registrationPage,name="registrationPage"),
    path('',loginPage,name="loginPage"),
    
]
