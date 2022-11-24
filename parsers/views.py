from django.template import loader
from django.http import HttpResponse
from .models import Fish
from .forms import FishParserForm
import requests

# Create your views here.
def index(request):
    template = loader.get_template('parsers/index.html')
    return HttpResponse(template.render({'form': FishParserForm()}, request))

def create(request):
    url = request.POST.get("link", "")
    result = requests.get(url)
    breakpoint()
    return HttpResponse("Completed parse")