from django.shortcuts import render
import numpy as np
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def root(request):
    return render(request, 'root.html')

def hello(request):
    username = 'minsu'

    context = {
        'username': username,
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menus = ['김밥', '라면', '돈까스']

    pick = random.choice(menus)


    context = {
        'pick': pick
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    lotto = random.sample(range(1, 46), 6)

    context = {
        'lotto': lotto
    }

    return render(request, 'lotto.html', context)
