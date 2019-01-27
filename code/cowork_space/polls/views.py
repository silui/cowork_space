import os
from django.http import HttpResponse


def index(request):
    doodoo = os.environ['wai']
    return HttpResponse("Hello, world. You're at the polls index." + doodoo)

def test(request):
    return HttpResponse("this is the test page")

