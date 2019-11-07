import json

from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app import numpy_encoder
from app.Federated import FederatedServer

import logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def index(request):
    logger.info("request index")
    return HttpResponse("index ok", status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def weight(request):
    if request.method == 'GET':
        global_weight = FederatedServer.get_avg()
        global_weight_to_json = json.dumps(global_weight, cls=numpy_encoder.NumpyEncoder)
        return HttpResponse(global_weight_to_json, status.HTTP_200_OK)

    elif request.method == 'PUT':
        print("request PUT weight")
        json_data = JSONParser().parse(request)
        FederatedServer.update(json_data)
        return HttpResponse("Request PUT OK", status.HTTP_200_OK)

    else :
        print("request OTHER weight")
        return HttpResponse("Request OK", status.HTTP_200_OK)