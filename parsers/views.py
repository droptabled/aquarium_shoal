from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    return HttpResponse("Aquarium Shoal Data Aggregator")

def create(request):
    url = request.POST.get("link", "")
    result = requests.get(url)
    breakpoint()