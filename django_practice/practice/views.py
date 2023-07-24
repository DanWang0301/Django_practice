from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def anime(request):
    return render(request,'anime_list.html')