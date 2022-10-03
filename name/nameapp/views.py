# from turtle import title
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def String_converter(request):
    enter_the_string=(request.POST['enter_the_string'])
    # n2=int(request.POST['num2'])
    # res=n1+n2
    if 'converter' in request.POST:
        res=enter_the_string.swapcase()
    # elif 'lower' in request.POST:
    #     res=enter_the_string.lower()
    elif 'title' in request.POST:
        res=enter_the_string.title()
    # elif 'mul' in request.POST:
    #     res=n1*n2
    # elif 'mod' in request.POST:
    #     res=n1%n2
    return render(request,'result.html',{'result':res})
