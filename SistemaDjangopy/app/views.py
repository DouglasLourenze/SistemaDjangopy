from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app import templates
# Create your views here.

def index(Request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello world!")
    #return render(Request, 'templates/home.html', context)