from django.shortcuts import render
from .forms import productsView
# Create your views here.

def index(request):
    form=productsView()

    if request.method == "POST":
        form = productsView(request.POST)

        if form.is_valid():
            form.save()

    return render (request,"index.html",{'form':form})