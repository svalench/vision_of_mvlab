from .models import *
from rest_framework import serializers

class CorparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corparation
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class LunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lunch
        fields = '__all__'

class AgreagatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreagat
        fields = '__all__'

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'