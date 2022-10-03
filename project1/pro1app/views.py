from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def Ave(request):
    Ave={'name':'This is Avengers that crossed all the records in 2020'}
    return render(request,"Ave.html",context=Ave)

def KGF2(request):
    KGF={'name':'This is Avengers that crossed all the records in 2020'}
    return render(request,"KGF2.html",context=KGF)