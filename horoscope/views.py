from django.shortcuts import render, redirect, reverse
import requests
from django.contrib.auth.models import User
from .models import Person


signs=['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagitarus', 'capricorn', 'aquarius', 'pisces']
dates=['21 Mar-19 Apr', '20 Apr-20 May', '21 May-20 Jun', 
    '21 Jun- 22 Jul', '23 Jul-22 Aug', '23 Aug-22 Sep',
    '23 Sep-22 Oct', '23 Oct-21 Nov', '22 Nov-21 Dec',
    '22 Dec-19 Jan', '20 Jan-18 Feb', '19 Feb-20 Mar']
color = ['lightblue', 'lightcoral', 'cyan', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'rgb(226, 81, 231)', '#8bbe1b', 'lightsteelblue', '#40e0d0','aquamarine']
images=['nature', 'underwater', 'coral','galaxy', 'star', 'colors', 'butterfly', 'asthetic', 'lifestyle']
# Create your views here.
def home(request):
    tmp = {}
    r = requests.post('https://zenquotes.io/api/random')
    for i in range(12):
        tmp[signs[i]] = {'color':color[i], 'date':{'from':dates[i].split('-')[0],'to':dates[i].split('-')[1]}}
    context={'app':'home','sign_dates': tmp, 
    'signs':signs,
    'quote':eval(r._content)[0],
    'images':images}

    if request.method=='POST':
        name = request.POST['name']
        dob = request.POST['DOB']
        p = Person.create(name, dob)
        p.save()
        tmp = [(dates[i],dates[i+1]) for i in range(-3,9)]
        mon = eval(dob.split('-')[1].lstrip('0'))
        day = eval(dob.split('-')[2].lstrip('0'))
        ran = tmp[mon-1]
        partition = [eval(ran[0].split('-')[1].lstrip().split(' ')[0]),eval(ran[1].split('-')[0].lstrip().split(' ')[0])]
        if day in range(0,partition[0]):
            rang = ran[0]
        elif day in range(partition[1],32):
            rang = ran[1]
        else:
            rang=None
        context['output_sign']=dict(zip(dates,signs))[rang] if rang else 'Enter Valid Date'

        return render(request,'index.html',context=context)
    else:
        context['output_sign']='None'
        return render(request,'index.html',context=context)

def chooseZodiac(request):
    tmp = {}
    for i in range(12):
        tmp[signs[i]] = {'color':color[i], 'date':{'from':dates[i].split('-')[0],'to':dates[i].split('-')[1]}}
    context={'app':'horoscope','sign_dates': tmp, 
    'signs':signs,}
    return render(request, 'chooseZodiac.html', context=context)

def horo(request, sign='aries', day='today'):
    params = (
    ('sign', sign),
    ('day', day),
    )

    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    content = eval(r._content)
    context={'app':'horoscope','sign': sign, 'day': day,
    'sign_dates':dict(zip(list(range(12)),dates)),
    'signs':signs,
    'current_date':content['current_date'],
    'description':content['description'],
    'compatibility':{
    'Match':content['compatibility'],
    'Mood':content['mood']},
    'about':{
    'Lucky Color':content['color'].lower(),
    'Lucky Number':content['lucky_number'],
    'Lucky Time':content['lucky_time']
        }
    }

    return render(request, 'horoscope.html', context=context)

def imgs(request):
    return render(request, 'many.html', context={'app':'images','signs':signs, 'images':images})

def quotes(request):
    params=(('author','chanakya'),)
    r = requests.post('https://zenquotes.io/api/random')
    return render(request, 'many.html', context={'app':'quotes',
    'signs':signs,
    'quote':eval(r._content)[0]})

def svg_edit(request):
    svg = open('C:/Users/Admin/Desktop/Logo .svg')
    if request.method == 'POST':
        color1 = request.POST['color1']
        color2 = request.POST['color2']
        color3 = request.POST['color3']
        color4 = request.POST['color4']
        color5 = request.POST['color5']
        color6 = request.POST['color6']
    else:
        color1='#ff0000'
        color2='#ffff00'
        color3='#ff0000'
        color4='#ffffff'
        color5='#ff0000'
        color6='#ff8000'
    data = svg.read()
    data = data.replace('{{color1}}',color1)
    data = data.replace('{{color2}}',color2)
    data = data.replace('{{color3}}',color3)
    data = data.replace('{{color4}}',color4)
    data = data.replace('{{color5}}',color5)
    data = data.replace('{{color6}}',color6)
    return render(request, 'for_svg.html', {'app':'home', 'svg':str(data)})

    

    

