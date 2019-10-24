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
        print("request GET weight : ")
        FederatedServer.get_avg()
        return HttpResponse(FederatedServer.get_avg(), status.HTTP_200_OK)

    elif request.method == 'PUT':
        print("request PUT weight")
        data = JSONParser().parse(request)
        print("PUT data : {}".format(data))
        FederatedServer.update(data)
        return HttpResponse("Request PUT OK", status.HTTP_200_OK)

    else :
        print("request OTHER weight")
        return HttpResponse("Request OK", status.HTTP_200_OK)