from django.db import models

# Create your models here.

class JobModel(models.Model):
    company_name=models.CharField(max_length=100,blank=False)
    company_mail=models.EmailField(blank=False)
    job_title= models.CharField(max_length=30,blank=False)
    job_desc=models.CharField(max_length=250,blank=False)
    location=models.CharField(max_length=30,blank=False)
    salary=models.IntegerField(blank=False)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_name

