from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class People(models.Model):
    firstname = models.CharField(max_length=40,null=False,blank=False)
    lastname =models.CharField(max_length=40,null=True,blank=False)
    email = models.EmailField(max_length = 50,unique=True)
    phone = models.CharField(max_length=13,null=False,blank=False,unique=True,validators=[MinLengthValidator(10)])
    #This field will be automatically populated 
    create = models.DateTimeField(auto_now_add=True)
    #Role options
    role=[
        ("member","Regular - Can't delete members"),
        ("admin","Admin - Can delete members")
    ]
    
    #default role is member
    choice=models.CharField(choices=role,default="member",max_length=20)
    #capitalize first letter in every word for firstname and lastname 
    def clean(self):
        self.firstname=self.firstname.capitalize().title()
        self.lastname = self.lastname.capitalize().title()



   
    
    #String representation of the model
    def __str__(self):
        return self.firstname
    
    #The list will be ordered according to the time they were created 
    class Meta:
        ordering = ['create']




