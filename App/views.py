# Description: This file is used to take HTTPS requests and return HTTP responses.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializer import AccountSerializer, PropertySerializer, DefaultSerializer
from .models import *
import json


# Create your views here.
def main(request):
  template = loader.get_template('ApiCall.html')
  accounts = Account.objects.using('account-db').all()
  # return HttpResponse(template.render())
  return render(request, 'ApiCall.html', {'accounts': accounts})
    
class DefaultViewSet(viewsets.ModelViewSet):
    queryset = Default.objects.all()
    serializer_class = DefaultSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


@api_view(['GET', 'POST'])
def get_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)
    elif request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    else:
        pass

@csrf_exempt
def create_entry(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latest_account = Account.objects.last()
            if latest_account:
                new_account_id = latest_account.account_id + 1  # Increment by 1
            else:
                new_account_id = 1 
            account = Account(
                account_id=new_account_id,
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                date_of_birth=data['date_of_birth']
            )
            account.save(using='account-db')  # Specify the database to use

            return JsonResponse({'status': 'success', 'message': 'User created successfully', 'account_id': new_account_id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add_entry(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            account_id = data.get('account_id')
            if not Account.objects.filter(account_id=account_id).exists():
                account = Account(
                    account_id=account_id,
                    username=data['username'],
                    password=data['password'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    date_of_birth=data['date_of_birth']
                )
                account.save(using='account-db')

                return JsonResponse({'status': 'success', 'message': 'User created successfully', 'account_id': account_id})
            else:
                return JsonResponse({'status': 'error', 'message': 'User already exists'}, status=409)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_entry(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            account_id = data.get('account_id')
            if account_id:
                account = Account.objects.get(account_id=account_id)
                account.delete()
                return JsonResponse({'status': 'success', 'message': 'User deleted successfully', 'account_id': account_id})
            else:
                return JsonResponse({'status': 'error', 'message': 'Nothing to delete'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def get_input(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            account_id = data.get('account_id')
            return JsonResponse({'status': 'success', 'message': 'User Input', 'account_id': account_id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_latest_entry(request):
    if request.method == 'DELETE':
        try:
            latest_entry = Account.objects.last()
            if latest_entry:
                latest_entry.delete()
                return JsonResponse({'status': 'success', 'message': 'Latest entry deleted'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Nothing to delete'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_all_entry(request):
    if request.method == 'DELETE':
        try:
            count, _ = Account.objects.all().delete()
            if count > 0:
                return JsonResponse({'status': 'success', 'message': f'{count} entries deleted'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Nothing to delete'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def update_entry(request):
    if request.method == "UPDATE":
        try:
            data = json.loads(request.body)
            account_id = data.get('account_id')

            if Account.objects.filter(account_id=account_id).exists():
                account = Account.objects.get(account_id=account_id)
                account.username = data['username']
                account.password = data['password']
                account.email = data['email']
                account.first_name = data['first_name']
                account.last_name = data['last_name']
                account.date_of_birth = data['date_of_birth']
                account.save(using='account-db')

                return JsonResponse({'status': 'success', 'message': 'User updated successfully', 'account_id': account_id})
            else:
                return JsonResponse({'status': 'error', 'message': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
