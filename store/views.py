import json
import uuid
from datetime import datetime

from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from rest_framework.decorators import api_view

from .models import *


@api_view(['POST'])
def issue_receipt(request):
    try:
        json_data = json.loads(request.body)
        userid = uuid.UUID(json_data['userId'])
        username = json_data['username']
        payment_type = json_data['paymentType']
        payment = Payment.objects.get(userId=userid)
        if payment_type is StoreItem.PaymentType.AD:
            payment.adWatched += 1
            payment.log += 'Ad watched at ' + str(datetime.now()) + '\n'
        else:
            payment.pricePaid += 1
            payment.receipts.add(Receipt.objects.create(userId=userid, username=username,
                                                        name=json_data['name'], description=json_data['description'],
                                                        reward=json_data['reward'], rewardType=json_data['rewardType'],
                                                        price=json_data['price'], paymentType=payment_type))
            payment.log += 'Payment done at ' + str(datetime.now()) + '\n'
        payment.save()
        return HttpResponse(json.dumps({"status": "success"}))
    except (KeyError, ValueError, json.decoder.JSONDecodeError):
        return HttpResponseServerError(json.dumps({"status": "badRequest", "error": "Malformed data"}))
    except Payment.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"status": "invalidAuth", "error": "Payment does not exist"}))
