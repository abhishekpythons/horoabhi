from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    params = (
    ('sign', 'aries'),
    ('day', 'today'),
    )

    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    content = eval(r._content)
    return render(request, 'index.html', context = {'content':content})