from django import forms
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"
        exclude = ['Created_By']
        