from django.shortcuts import render

# Create your views here.
def index(request):
    details={
        'movies':['a','b','c','d','e'],
        'information':[
            {'name':'kavya','address':'abc','phone':68787980},
            {'name':'keer','address':'ylk','phone':6797980}        ],
    'std_details':[
        { 'name':'meenal','marks':69,'grade':'B','branch':'cs'},
        { 'name':'me','marks':56,'grade':'B','branch':'cs'},
        { 'name':'nal','marks':79,'grade':'B','branch':'cs'},
        { 'name':'meens','marks':39,'grade':'B','branch':'cs'}
    ]
     
    }
    return render(request,'index.html',context=details)