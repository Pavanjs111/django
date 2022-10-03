from django.urls import path 
from schoolapp.views import SchoolCreateView, SchoolListView
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailsView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update')

]