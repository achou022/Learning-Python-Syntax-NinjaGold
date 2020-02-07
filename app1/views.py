from django.shortcuts import render, redirect
import random
from time import strftime, localtime

# Create your views here.
def ninjaMenu(request):
    if 'playerGold' not in request.session:
        request.session['playerGold']=0
    if 'earningLog' not in request.session:
        request.session['earningLog']=[]
    return render(request, "ninjaGold.html")

def processMoney(request):
    if('farm'==request.POST['location']):
        earning=randInt(10,20)
    elif('cave'==request.POST['location']):
        earning=randInt(5,10)
    elif('house'==request.POST['location']):
        earning=randInt(2,5)
    elif('casino'==request.POST['location']):
        earning=randInt(-50,50)
    print('money processed')
    request.session['playerGold']+=earning
    time=strftime("%m-%d %H:%M:%S %p", localtime())
    if earning>=0:
        result=f"<p style=\"color: green;\">Earned {earning} from the {request.POST['location']}! ({time})</p>"
    else:
        result=f"<p style=\"color: red;\">Entered a {request.POST['location']} and lost {earning} golds... Ouch...({time})</p>"
    request.session['earningLog'].append(result)
    request.session.save()
    return redirect('/')

def randInt(min=0, max=100):
    return round(random.random()*(max-min)+min)

def reset(request):
    request.session['playerGold']=0
    request.session['earningLog']=[]
    return redirect('/')