import json

import numpy as np
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app.Federated import FederatedServer


@api_view(['GET', 'PUT'])
def weight(request):
    if request.method == 'GET':

        '''
        global_weight = FederatedServer.get_avg()
        if len(global_weight) == 0:
            global_weight = None
        '''
        temp = FederatedServer.get_avg()
        print("temp : ", len(temp), len(temp[0]), len(temp[1]))
        global_weight = json.dumps(FederatedServer.get_avg())

        #print("request get weight : {}".format(global_weight))
        return HttpResponse(global_weight, status.HTTP_200_OK)

    elif request.method == 'PUT':
        print("request PUT weight")
        data = JSONParser().parse(request)

        data_restored = np.asarray(data)
        #print("PUT data : {}, {}, {}, {}".format(type(data), len(data), len(data[0]), len(data[1])))
        print("PUT data : {}, {}, {}, {}".format(type(data_restored), len(data_restored), len(data_restored[0]), len(data_restored[1])))
        FederatedServer.update(data_restored)
        return HttpResponse("Request PUT OK", status.HTTP_200_OK)

    else :
        print("request OTHER weight")
        return HttpResponse("Request OK", status.HTTP_200_OK)