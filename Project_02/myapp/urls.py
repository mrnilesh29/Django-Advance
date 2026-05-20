from django.urls import path
from . import views 

urlpatterns = [
    path("home/" , views.home , name= "Home_page"), 
    path("contact/" , views.contact, name="contact_page")
    
]

