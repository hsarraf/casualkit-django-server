import json
import uuid

from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from rest_framework.decorators import api_view

from score.models import Score


@api_view(['POST'])
def update(request):
    try:
        json_data = json.loads(request.body)
        user_id = uuid.UUID(json_data['userId'])
        score = Score.objects.get(userId=user_id)
        if json_data['coin'] is not None:
            score.coin = json_data['coin']
        if json_data['gem'] is not None:
            score.gem = json_data['gem']
        if json_data['cup'] is not None:
            score.cup = json_data['cup']
        if json_data['score'] is not None:
            score.score = json_data['score']
        if json_data['level'] is not None:
            score.level = json_data['level']
        if json_data['rank'] is not None:
            score.rank = json_data['rank']
        if json_data['xp'] is not None:
            score.xp = json_data['xp']
        if json_data['fan'] is not None:
            score.fan = json_data['fan']
        score.save()
        return HttpResponse(json.dumps({"status": "success"}))
    except (KeyError, ValueError, json.decoder.JSONDecodeError):
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": "Malformed data"}))
    except Score.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"status": "doesNotExist", "error": "Score does not exist"}))
