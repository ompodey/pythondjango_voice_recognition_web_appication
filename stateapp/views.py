from django.shortcuts import render
from stateapp.models import Horse




def index(request):
    return render(request,"index.html")

def contributers(request):
    return render(request,"contributers.html")

def sourcecode(request):
    return render(request,"sourcecode.html")

def datastore(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        suggestion=request.POST.get("suggestion")
        
        datastore=Horse(name=name,email=email,suggestion=suggestion) 
        datastore.save()                                                                                                                                      
    return render(request,"datastore.html")

        
        
