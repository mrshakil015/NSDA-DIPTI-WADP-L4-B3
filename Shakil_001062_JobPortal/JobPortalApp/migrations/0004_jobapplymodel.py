# Generated by Django 5.0.6 on 2024-07-08 10:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortalApp', '0003_rename_createdby_jobmodel_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=100, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantuser', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobPortalApp.jobmodel')),
            ],
        ),
    ]