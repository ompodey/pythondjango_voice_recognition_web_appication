from django.db import models
class Horse(models.Model):
    name=models.CharField(max_length=122,default="",null=True)
    email=models.CharField(max_length=122,default="",null=True)
    suggestion=models.CharField(max_length=122,default="",null=True)

    def __str__(self):
        return self.name
    

# Create your models here.
