from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app import templates
from .forms import Formcadastroatividade
from app.models import cadastroatividade
# Create your views here.

def index(request):
    #template = loader.get_template('app/index.html')
    #return HttpResponse(template.render())
    #return HttpResponse("Hello world!")
    #return render(Request, 'templates/home.html', context)


    form= Formcadastroatividade(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
    atividades = cadastroatividade.objects.all()    
    return render(request, 'app/index.html', {'atividade':atividades}, context)
