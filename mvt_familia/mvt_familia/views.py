from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render

def familia(request):
    return render(request,'familia.html', context={})