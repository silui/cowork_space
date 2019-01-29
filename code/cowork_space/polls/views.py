import os
from django.http import HttpResponse
from multiprocessing import Pool
from multiprocessing import cpu_count
import math

pool = Pool(processes)
    

def f(x):
    for doodoo in range (x):
        return_this=math.factorial(doodoo)
    return return_this


def index(request):
    doodoo = os.environ['wai']
    return HttpResponse("Fourth code pipeline test" + doodoo)

def test(request,multipler=2):
    if(multipler>5000):
        return HttpResponse("multipler too big")
    pool.map(f, [multipler,multipler])
    return HttpResponse("this is the test page")

