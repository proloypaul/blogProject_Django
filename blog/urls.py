from django.urls import path
from . import views

urlpatterns = [
    # path('/blog', views.blogPageTwo, name="homePageTwo"),
    path('', views.home, name="homePage"),
]
