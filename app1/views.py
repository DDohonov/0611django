from django.shortcuts import render
from random import randint

# Create your views here.

from .models import First_model

def view (request):
    a = randint(1,4)
    obj = First_model.objects.get(pk=a)
    context = {
        "obj": obj,

    }

    return render(request, "app1/base.html", context = context)