from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('home',views.index,name='home'),
    path('contributers',views.contributers,name='contributers'),
    path('sourcecode',views.sourcecode,name='sourcecode'),
    path('datastore',views.datastore,name='datastore'),
    
]