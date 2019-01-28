from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import User
from backend.models import Sport
from backend.serializers import SportSerializer
import requests

# Create your views here.

class SportList(APIView):

    def getEventTypes(self,request):
        appKey = "oFh5V6gzpQdgwlCZ"
        sessionKey = "/ee/Nqvle3tvEaXwIkQ0Shry7rOha9qY5pKt9uAycvM="

        headers = { 'X-Application' : appKey, 'X-Authentication' : sessionKey,'content-type' : 'application/json' }
        event_type_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEventTypes", "params": {"filter":{ }}, "id": 1}'
        response = requests.post("https://api.betfair.com/exchange/betting/json-rpc/v1",data=event_type_req,headers=headers)
        return response;
    def get (self, request):
        sports = Sport.objects.all()
        #res = self.getEventTypes(request)
        serializer = SportSerializer(sports,many = True)
        return Response(serializer.data)

class CompetitionList(APIView):

    def getCompetitions(self,request):
        appKey = "oFh5V6gzpQdgwlCZ"
        sessionKey = "/ee/Nqvle3tvEaXwIkQ0Shry7rOha9qY5pKt9uAycvM="

        headers = { 'X-Application' : appKey, 'X-Authentication' : sessionKey,'content-type' : 'application/json' }
        event_type_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listCompetitions", "params": {"filter":{"eventTypeIds":[2]}}, "id": 1}'
        response = requests.post("https://api.betfair.com/exchange/betting/json-rpc/v1",data=event_type_req,headers=headers)
        return response;

    def get (self, request):
        #sports = Sport.objects.all()
        res = self.getCompetitions(request)
        #serializer = SportSerializer(sports,many = True)
        #return Response(serializer.data)
        return Response(res)
