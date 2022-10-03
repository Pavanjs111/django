from email import message
from django.shortcuts import render

# Create your views here.
def index(request):
    my_dictionary={'insert_me':'i am not in danger, i am the danger','number':100}
    return render(request,"index.html",context=my_dictionary)

def other(request):
    my_dictionary={'insert_me':'i am not in danger, i am the danger'}
    return render(request,"other.html",context=my_dictionary)

def relative(request):
    message={'msg':'i am the devil in my world'}
    return render(request,"relative.html",context=message)

def about(request):
    message={'insert_me':'i love coding and coding likes me'}
    return render(request,"about.html",context=message)

def extra(request):
    return render(request,"extra.html")