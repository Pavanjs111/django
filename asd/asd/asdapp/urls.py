from django.urls import path
from asdapp import views

app_name = "asdapp"

urlpatterns=[
    
    path('user_login/',views.user_login,name="login"),
    
    path('index/',views.index,name="index"),
]