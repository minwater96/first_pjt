import random
import numpy as np
from faker import Faker
from django.shortcuts import render
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

def username(request, name):
    context = {
        'name': name,
    }

    return render(request, 'username.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'result': result
    }

    return render(request, 'cube.html', context)

def posts(request):
    fake = Faker()

    fake_posts = []

    for i in range(100):
        fake_posts.append(fake.text())

    context = {
        'fake_posts': fake_posts
    }

    return render(request, 'posts.html', context)