from bs4 import BeautifulSoup
from django.template import loader
from django.http import HttpResponse
from .models import Fish
from .forms import FishParserForm
from .llm_parser import LLMParser
import requests

# Create your views here.
def index(request):
    template = loader.get_template('parsers/index.html')
    return HttpResponse(template.render({'form': FishParserForm()}, request))

def create(request):
    fish_id = request.POST.get("fish", "")
    fish = Fish.objects.get(id=fish_id)

    url = request.POST.get("url", "")
    result = requests.get(url, allow_redirects=True)

    html_content = BeautifulSoup(result.content, features="html.parser")
    tables = html_content.find_all("table")
    text = ""

    # all tables
    #for table in tables:
    #    text += " " + table.get_text(" ")

    # first table
    text += tables[0].get_text(" ")
    parsed_json = LLMParser.parse(text)
    breakpoint()

    return HttpResponse("Completed parse")