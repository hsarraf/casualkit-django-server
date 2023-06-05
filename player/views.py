import json
from datetime import datetime

from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from rest_framework.decorators import api_view

from .utils import *
from userProfile.models import UserProfile
from social.models import Social
from score.models import Score
from store.models import Payment
from dailyChallenge.models import DailyChallenge


# @cache_page(5)
@api_view(['GET'])
def verify(request):
    username = request.GET['username']
    if Player.objects.filter(username=username).exists():
        return HttpResponse(json.dumps({"status": "success"}))
    else:
        return HttpResponseNotFound(json.dumps({"status": "fail", "error": "username doesn't exist"}))


@api_view(['POST'])
def register(request):
    try:
        json_data = json.loads(request.body)
        username = json_data['username']
        gender = json_data['gender']
        if not Player.objects.filter(username=username).exists():
            player = Player.objects.create(username=username, log='Account created at ' + str(datetime.now()) + '\n')
            player.userProfile = UserProfile.objects.create(userId=player.userId, username=username, gender=gender, log='Profile created at ' + str(datetime.now()) + '\n')
            player.social = Social.objects.create(userId=player.userId, username=username, socialId=player.userId.hex, log='Social created at ' + str(datetime.now()) + '\n')
            player.score = Score.objects.create(userId=player.userId, username=username, log='Score created at ' + str(datetime.now()) + '\n')
            player.payment = Payment.objects.create(userId=player.userId, username=username, log='Payment created at ' + str(datetime.now()) + '\n')
            player.dailyChallenge = DailyChallenge.objects.create(userId=player.userId, username=username, log='Daily Challenge created at ' + str(datetime.now()) + '\n')
            player.save()
            return HttpResponse(json.dumps({"status": "success", "payload": player.get()}))
        else:
            return HttpResponse(json.dumps({"status": "alreadyExists", "error": "Username already taken"}), status=400)
    except (KeyError, ValueError, json.decoder.JSONDecodeError):
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": "Malformed data"}))


@api_view(['POST'])
def login(request):
    try:
        json_data = json.loads(request.body)
        userid = json_data['userId']
        player = Player.objects.get(userId=userid)
        return HttpResponse(json.dumps({"status": "success", "payload": player.get()}))
    except (KeyError, ValueError, json.decoder.JSONDecodeError):
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": "Malformed data"}))
    except Player.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"status": "invalidAuth", "error": "Username does not exist"}))
