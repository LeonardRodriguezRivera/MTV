from multiprocessing import context
from django.shortcuts import render
from familia.models import Familia


def familia(request):
    familia = Familia.objects.all()
    context = {

        'familia': familia
    }


    return render(request,'familia.html', context=context)
