
from django.urls import path

from .import views

urlpatterns = [

    #path('',views.about1,name='about1'),
    path('',views.contact,name='contact'),
    #path('calculate/', views.calculate, name='calculate'),
    #path('contact/',views.contact,name='contact'),
    #path('details/',views.details,name='details'),
    #path('thanks/',views.thanks,name='thanks'),
]
