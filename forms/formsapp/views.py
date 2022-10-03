from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def formsapp(request):
    form=forms.emp()
    if request.method =='POST':
        form=forms.emp(request.POST)

        if form.is_valid():
            print("validation successful")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['text'])

    return render(request,'fv.html',{'form':form})
