import os
from django.http import HttpResponse

def f(x):
    return_this=2
    for doodoo in range(x):
        return_this=return_this*return_this
    return return_this


def index(request):
    doodoo = os.environ['wai']
    return HttpResponse("Second code pipeline test" + doodoo)

def test(request,multipler=2):
    if(multipler>20):
        return HttpResponse("multipler too big")
    return HttpResponse("this is the test page\n"+str(f(multipler)))

