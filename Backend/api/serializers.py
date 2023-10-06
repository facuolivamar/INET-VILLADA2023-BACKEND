from rest_framework import serializers
from BackendApp.models import Doctor, Calls, Patient, Room, BloodType, SocialPlan

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = '__all__'

class SocialPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlan
        fields = '__all__'
