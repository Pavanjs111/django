from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def caulator(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    # res=n1+n2
    if 'add' in request.GET:
        res=n1+n2
    elif 'sub' in request.POST:
        res=n1-n2
    elif 'div' in request.POST:
        res=n1/n2
    elif 'mul' in request.POST:
        res=n1*n2
    elif 'mod' in request.POST:
        res=n1%n2
    return render(request,'result.html',{'result':res})

# def sub(request):
#     n1=int(request.POST['num1'])
#     n2=int(request.POST['num2'])
#     res=n1-n2
#     return render(request,'result.html',{'result1':res})

# def div(request):
#     n1=int(request.POST['num1'])
#     n2=int(request.POST['num2'])
#     res=n1/n2
#     return render(request,'result.html',{'result2':res})

# def mul(request):
#     n1=int(request.POST['num1'])
#     n2=int(request.POST['num2'])
#     res=n1*n2
#     return render(request,'result.html',{'result3':res})

# def Mod(request):
#     n1=int(request.POST['num1'])
#     n2=int(request.POST['num2'])
#     res=n1%n2
#     return render(request,'result.html',{'result4':res})