from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'Pavan'})

def two(request):
    my_dictionary={'insert_me':'be good, do good'}
    return render(request,'second.html',context=my_dictionary)

