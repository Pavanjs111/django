# from multiprocessing import get_context
from django.shortcuts import render
from . import models
from telnetlib import DET
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView

# Create your views here.
# def index(request):
#     return render(request,'index.html')
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    #Here the schools name we have to give the same name in school_list.html inside for loop
    context_object_name = 'schools'
    model = models.school

class SchoolDetailsView(DetailView):
    context_object_name = 'school_detail'
    model = models.school
    template_name = 'schoolapp/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name_of_the_school','prinicipal','adress')
    model=models.school

class SchoolUpdateView(UpdateView):
    fields=('name_of_the_school','prinicipal')
    model=models.school 

class SchoolDeleteView(DeleteView):
    fields=('name_of_the_school','prinicipal')
    model=models.school 