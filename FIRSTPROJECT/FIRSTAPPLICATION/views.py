from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def display(request):
    #return HttpResponse("Welcome to innovation with python")

#def content(request):
   # return HttpResponse("Welcome to Java training with Consult Add")

def design(request):
    dict1= {'use_me': "This is coming from inside a template inside FIRSTAPPLICATION"}
    return render(request, 'FIRSTAPPLICATION/design.html', context=dict1)
