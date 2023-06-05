import json
from datetime import datetime

from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from rest_framework.decorators import api_view

from .models import UserProfile


@api_view(['POST'])
def update(request):
    try:
        json_data = json.loads(request.body)
        userid = json_data['userId']
        profile = UserProfile.objects.get(userId=userid)
        if json_data['emailAddress'] is not None:
            profile.coin = json_data['emailAddress']
        if json_data['displayName'] is not None:
            profile.coin = json_data['displayName']
        if json_data['gender'] is not None:
            profile.coin = json_data['gender']
        if json_data['avatar'] is not None:
            profile.coin = json_data['avatar']
        profile.log += 'Updated at ' + str(datetime.now()) + '\n'
        profile.save()
        return HttpResponse(json.dumps({"status": "success"}))
    except (KeyError, ValueError, json.decoder.JSONDecodeError):
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": "Malformed data"}))
    except UserProfile.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"status": "doesNotExist", "error": "Profile does not exist"}))