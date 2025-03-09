# Description: This file is used to take HTTPS requests and return HTTP responses.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse
from .serializer import AccountSerializer, PropertySerializer, DefaultSerializer
from .models import *
import json


# Create your views here.
def main(request):
  template = loader.get_template('ApiCall.html')
  return HttpResponse(template.render())

class DefaultViewSet(viewsets.ModelViewSet):
    queryset = Default.objects.all()
    serializer_class = DefaultSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

@api_view(['GET'])
def get_account(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.data, status=400)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        account = Account(
            account_id=data['account_id'],
            username=data['username'],
            password=data['password'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth']
        )
        account.save(using='account-db')  # Specify the database to use
        return HttpResponse({'status': 'success'})
    return HttpResponse({'status': 'error'}, status=400)