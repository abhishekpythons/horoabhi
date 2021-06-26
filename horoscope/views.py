from django.shortcuts import render
import requests
from django.contrib.auth.models import User

signs=['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagitarus', 'capricorn', 'aquarius', 'pisces']
dates=['21 Mar-19 Apr', '20 Apr-20 May', '21 May-20 Jun', 
    '21 Jun- 22 Jul', '23 Jul-22 Aug', '23 Aug-22 Sep',
    '23 Sep-22 Oct', '23 Oct-21 Nov', '22 Nov-21 Dec',
    '22 Dec-19 Jan', '20 Jan-18 Feb', '19 Feb-20 Mar']
color = ['lightblue', 'lightcoral', 'cyan', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'rgb(226, 81, 231)', 'lightsteelblue', 'yellow', 'lime','aquamarine']
# Create your views here.
def home(request):
    tmp = {}
    r = requests.post('https://zenquotes.io/api/random')
    for i in range(12):
        tmp[signs[i]] = {'color':color[i], 'date':{'from':dates[i].split('-')[0],'to':dates[i].split('-')[1]}}
    context={'app':'home','sign_dates': tmp, 
    'signs':signs,
    'quote':eval(r._content)[0]}
    return render(request,'index.html',context=context)

def chooseZodiac(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['name'], 'lennon@thebeatles.com', 'johnpassword')

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
    return render(request, 'many.html', context={'app':'images','signs':signs})

def quotes(request):
    params=(('author','chanakya'),)
    r = requests.post('https://zenquotes.io/api/random')
    return render(request, 'many.html', context={'app':'quotes',
    'signs':signs,
    'quote':eval(r._content)[0]})
