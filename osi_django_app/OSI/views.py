from django.shortcuts import render
from django.views.generic import CreateView
from .models import soc, osc, univ_soc_woc

def index(request):
    return render(request, 'lists/index.html')

def soc_view(request):
    context = {
        'lists': soc.objects.filter(publish=True)
    }
    return render(request, 'OSI/soc.html', context)

class soc_create_view(CreateView):
    model = soc
    fields = ['title', 'soc_homepage', 'stripend', 'timeline']

def osc_view(request):
    context = {
        'lists': osc.objects.filter(publish=True)
    }
    return render(request, 'OSI/osc.html', context)

class osc_create_view(CreateView):
    model = osc
    fields = ['title', 'osc_homepage', 'awards', 'timeline']

def usocwoc(request):
    context = {
        'lists': univ_soc_woc.objects.filter(publish=True)
    }
    return render(request, 'OSI/u-soc-woc.html', context)

class u_woc_soc_create_view(CreateView):
    model = univ_soc_woc
    fields = ['title', 'homepage', 'awards', 'timeline']
