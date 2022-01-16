from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class People(models.Model):
    firstname = models.CharField(max_length=100,null=False,blank=False)
    lastname =models.CharField(max_length=100,null=True,blank=False)
    email = models.EmailField(max_length = 100,unique=True)
    phone = models.CharField(max_length=13,null=False,blank=False,unique=True)
    #This field will be automatically populated 
    create = models.DateTimeField(auto_now_add=True)
    #Role options
    role=[
        ("member","Regular - Can't delete members"),
        ("admin","Admin - Can delete members")
    ]
    #default role is member
    choice=models.CharField(choices=role,default="member",max_length=20)
    def clean(self):
        self.firstname=self.firstname.capitalize().title()
        self.lastname = self.lastname.capitalize().title()



   
    
    #String representation of the model
    def __str__(self):
        return self.firstname
    
    #The list will be ordered according to the time they were created 
    class Meta:
        ordering = ['create']




