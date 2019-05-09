from django.shortcuts import render
from django.views.generic import CreateView
from .models import soc

def index(request):
    return render(request, 'lists/index.html')

def soc_view(request):
    context = {
        'lists': soc.objects.all()
    }
    return render(request, 'lists/soc.html', context)

class soc_create_view(CreateView):
    model = soc
    fields = ['title', 'soc_homepage', 'stripend', 'timeline']

def osc(request):
    return render(request, 'lists/osc.html')

def usocwoc(request):
    return render(request, 'lists/u-soc-woc.html')
