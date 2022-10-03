from django.urls import path
from twoapp import views

urlpatterns=[
    path('', views.two)
    ]