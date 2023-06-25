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
    breakpoint
    return HttpResponse("Fish created")
