from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class JobPortalUser(AbstractUser):
    DisplayName = models.CharField(max_length=100,null=True)
    USERTYPE = [
        ('Recruiters','Recruiters'),
        ('Jobseekers','Jobseekers'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=100,null=True)
    
class RecruitersModel(models.Model):
    jobuser = models.OneToOneField(JobPortalUser,on_delete=models.CASCADE,related_name='recruitermodel',null=True)
    CompanyName = models.CharField(max_length=100,null=True)
    CompanyAddress = models.CharField(max_length=100,null=True)
    CompanyLogo = models.ImageField(upload_to='media/logo/',null=True)
    
class SeekerModel(models.Model):
    jobuser = models.OneToOneField(JobPortalUser,on_delete=models.CASCADE,related_name='seekermodel',null=True)
    SkillsSet = models.TextField(null=True)
    Resume = models.FileField(upload_to='media/resume/',null=True)
    
class JobModel(models.Model):
    Title = models.CharField(max_length=100,null=True)
    NumberOfOpenings = models.CharField(max_length=50,null=True)
    Category = models.CharField(max_length=50,null=True)
    JobDescription = models.TextField(null=True)
    SkillsSet = models.TextField(null=True)
    CreatedBy = models.ForeignKey(JobPortalUser,on_delete=models.CASCADE,null=True)
