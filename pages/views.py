from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from parsers.models import Fish
from .forms import FishForm

# Create your views here.
def index(request):
    template = loader.get_template('pages/index.html')
    fishes = Fish.objects.order_by('scientific_name')
    return HttpResponse(template.render({'fishes': fishes}, request))

def new(request):
    template = loader.get_template('pages/new.html')
    return render(request, 'pages/new.html', {'form': FishForm()})

def create(request):
    fish = Fish.objects.create(
        scientific_name=request.POST['scientific_name'],
        common_names=request.POST['common_names'].split(","),
    )

    template = loader.get_template('pages/fish.html')
    return HttpResponse(template.render({'fish': fish}, request))

def fish(request, fish_id):
    fish = Fish.objects.get(pk=fish_id)

    template = loader.get_template('pages/fish.html')
    return HttpResponse(template.render({'fish': fish}, request))
