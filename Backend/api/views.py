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
from BackendApp.models import Doctor, Calls, Patient, Room, BloodType, SocialPlan
from .serializers import DoctorSerializer, CallsSerializer, PatientSerializer, RoomSerializer, BloodTypeSerializer, SocialPlanSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class CallsViewSet(viewsets.ModelViewSet):
    queryset = Calls.objects.all()
    serializer_class = CallsSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer

class SocialPlanViewSet(viewsets.ModelViewSet):
    queryset = SocialPlan.objects.all()
    serializer_class = SocialPlanSerializer


