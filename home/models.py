from django.db import models
from django.contrib.auth.models import User,auth
from datetime import date

# Create your models here.
class Bus(models.Model):
    name=models.CharField(max_length=50)
    From=models.CharField(max_length=50,default='0')
    To=models.CharField(max_length=50,default='0')
    timefrom=models.CharField(max_length=50)
    timeto=models.CharField(max_length=50)
    date=models.DateField(blank=True,null=True)
    price=models.IntegerField(default=0)
    seatno=models.IntegerField(default=0)
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    

    
    duration=models.CharField(max_length=50)

    def  __str__(self):
      return self.name
    
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=250)  

    def  __str__(self):
      return self.name  
    
class book(models.Model):
    busid=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default=1)
    From=models.CharField(max_length=50,default=1)
    To=models.CharField(max_length=50,default=1)
    timefrom=models.CharField(max_length=50,default=1)
    timeto=models.CharField(max_length=50,default=1)
    date=models.DateField(blank=True,null=True)
    price=models.CharField(max_length=50,default=1)
    
    duration=models.CharField(max_length=50)
    seatno=models.CharField(max_length=50,default=1)
    tp=models.IntegerField(default=0)
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=1)


    @property
    def seatno_as_list(self):
        return self.seatno.split(',')
    def  __str__(self):
      return str(self.username)      