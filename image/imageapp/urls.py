from django.urls import path
from imageapp import views

urlpatterns=[
    path('',views.index)
]