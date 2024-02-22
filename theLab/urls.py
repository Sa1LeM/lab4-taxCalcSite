from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="index"),
    path("<int:num>", views.anyNumber, name="numbers"),
    path("taxrate", views.taxrate, name="taxrate")
]