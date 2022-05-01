from django.contrib import admin
from django.urls import path,include
from stateapp import views
urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.index,name='home'),
    path('contributers',views.contributers,name='contributers'),
    path('sourcecode',views.sourcecode,name='sourcecode'),
    path('datastore',views.datastore,name='datastore')
    
]