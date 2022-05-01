from django.db import models





class Horse(models.Model):
    name=models.CharField(max_length=122,default="",null=True)
    email=models.CharField(max_length=122,default="",null=True)
    suggestion=models.CharField(max_length=122,default="",null=True)
    



    