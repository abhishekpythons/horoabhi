from django.shortcuts import render
import requests


signs=['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagitarus', 'capricorn', 'aquarius', 'pisces']
dates=['Mar 21-Apr 19', 'Apr 20-May 20', 'May 21-Jun 20', 
    'Jun 21- Jul 22', 'Jul 23-Aug 22', 'Aug 23-Sep 22',
    'Sep 23-Oct 22', 'Oct 23-Nov 21', 'Nov 22-Dec 21',
    'Dec 22-Jan 19', 'Jan 20-Feb 18', 'Feb 19-March 20']
# Create your views here.
def home(request):
    context={'sign_dates':dict(zip(signs, dates))}
    return render(request, 'index.html', context=context)

def horo(request, sign='aries', day='today'):
    params = (
    ('sign', sign),
    ('day', day),
    )

    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    content = eval(r._content)
    context={'sign': sign, 'day': day,
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
