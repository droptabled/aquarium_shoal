from django.http import HttpResponse

def index(request):
    return HttpResponse("Aquarium Shoal Data Aggregator")

def create(request):
    return HttpResponse("Fish created")
