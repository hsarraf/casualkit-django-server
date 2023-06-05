import uuid
import json

import redis

from django.core.cache import caches

from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseNotFound
from rest_framework.decorators import api_view

from player.models import Player
from .utils import *
from .params import *


@api_view(['POST'])
def issue_ticket(request):
    try:
        json_data = json.loads(request.body)
        app_id = json_data['appId']
        #user_id = uuid.UUID(json_data['userId'])
        user_id = json_data['userId']
        player = Player.objects.get(username=user_id)
        if app_id == APP_ID:
            ticket = create_ticket()
            caches['redis'].set(player.username, ticket, TICKET_EXP_TIME, version='ticket')
            return HttpResponse(json.dumps({"status": "success", "payload": ticket}))
        else:
            return HttpResponseNotFound(json.dumps({"status": "invalidReq", "error": "Invalid request"}))
    except (KeyError, ValueError, json.decoder.JSONDecodeError) as ex:
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": str(ex)}))
    except (redis.exceptions.ConnectionError, redis.exceptions.DataError) as ex:
        return HttpResponseServerError(json.dumps({"status": "serverError", "error": str(ex)}))
    except Player.DoesNotExist as ex:
        return HttpResponseNotFound(json.dumps({"status": "doesNotExist", "error": str(ex)}))
    except Exception as ex:
        return HttpResponseNotFound(json.dumps({"status": "doesNotExist", "error": str(ex)}))
