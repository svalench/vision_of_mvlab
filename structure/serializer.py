from .models import *
from rest_framework import serializers

class Reserv_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reserv_1
        fields = '__all__'

class Reserv_2Serializer(serializers.ModelSerializer):
    parent = Reserv_1Serializer( read_only=True)
    class Meta:
        model = Reserv_2
        fields = '__all__'

class CorparationSerializer(serializers.ModelSerializer):
    parent = Reserv_2Serializer(read_only=True)
    class Meta:
        model = Corparation
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    parent = CorparationSerializer(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    parent = CompanySerializer(read_only=True)
    class Meta:
        model = Factory
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    parent = FactorySerializer(read_only=True)
    class Meta:
        model = Department
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    parent = DepartmentSerializer(read_only=True)
    class Meta:
        model = Shift
        fields = '__all__'

class LunchSerializer(serializers.ModelSerializer):
    parent = ShiftSerializer(read_only=True)
    class Meta:
        model = Lunch
        fields = '__all__'

class AgreagatSerializer(serializers.ModelSerializer):
    parent = DepartmentSerializer(read_only=True)
    class Meta:
        model = Agreagat
        fields = '__all__'

class SensorsSerializer(serializers.ModelSerializer):
    parent = AgreagatSerializer(read_only=True)
    class Meta:
        model = Sensors
        fields = '__all__'