# from pipes import Template
# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import View,TemplateView
# from django.http import HttpResponse

# Create your views here.


# this is function based views
# def index(request):
#     return HttpResponse('this is a function bases view')


# this is class based views
# class cbv(View):
#     def get(self,request):
#         return HttpResponse("<h1>Class based views are awesome</h1>")


# Template based views
class indexview(TemplateView):
    template_name='index.html'

