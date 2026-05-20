from . import views
from django.urls import path

urlpatterns = [
    path("home_page/", views.home_page, name="home_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("logout_page/<int:number>/", views.logout_page, name="logout_page"),
]

