from rest_framework.response import Response
from rest_framework.decorators import api_view
from BackendApp import models
from .serializers import *
from rest_framework import viewsets, permissions, generics
from django.db.models import Sum, Value, IntegerField, Q, Count, Case, When
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view





@api_view(["GET"])
def Test(request):
    if request.method == "GET":
       return Response("Test anda")
    return Response(status=405)



