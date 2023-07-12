from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'tourlist/tourlist1.html')

def indexone(request):
    return render(request, 'tourlist/tourlist1.html')

def indextwo(request):
    return render(request, 'tourlist/tourlist2.html')

def indexthree(request):
    return render(request, 'tourlist/tourlist3.html')