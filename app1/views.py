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
    if('farm'==request.POST['location']): #sets player's random earning depending on the location
        earning=randInt(10,20)
    elif('cave'==request.POST['location']):
        earning=randInt(5,10)
    elif('house'==request.POST['location']):
        earning=randInt(2,5)
    elif('casino'==request.POST['location']):
        earning=randInt(-50,50)
    request.session['playerGold']+=earning #update player gold count
    time=strftime("%m-%d %H:%M:%S %p", localtime())
    if earning>=0: #appends update log for the earning at then and that location
        request.session['earningLog'].append(f"<p style=\"color: green;\">Earned {earning} from the {request.POST['location']}! ({time})</p>")
    else:
        request.session['earningLog'].append(f"<p style=\"color: red;\">Entered a {request.POST['location']} and lost {earning} golds... Ouch...({time})</p>")
    request.session.save() #updates the list 
    return redirect('/')

def randInt(min=0, max=100):
    return round(random.random()*(max-min)+min)

def reset(request):
    request.session['playerGold']=0
    request.session['earningLog']=[]
    return redirect('/')