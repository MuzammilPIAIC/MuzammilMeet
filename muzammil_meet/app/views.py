from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time

# Create your views here.

def getToken(request):
    appId = 'd4ef5c28d9ed4a32b2a6cd0470abd093'
    appCertificate   =  '024b5a7b41634cdca01b1fa112113270'
    channelName  = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTime = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTime
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token, 'uid':uid},safe=False)



def Lobby(request):
    
    context = {"heading":'Lobby'}
    return render(request, 'app/lobby.html', context)

def Room(request):
    
    context = {}
    return render(request, 'app/room.html', context)



