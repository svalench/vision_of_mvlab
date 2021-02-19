from .models import *
from rest_framework import serializers

class Reserv_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reserv_1
        fields = '__all__'

class Reserv_2Serializer(serializers.ModelSerializer):
    parents = Reserv_1Serializer(source='parent', read_only=True)
    class Meta:
        model = Reserv_2
        fields = '__all__'

class CorparationSerializer(serializers.ModelSerializer):
    parents = Reserv_2Serializer(source='parent',read_only=True)
    class Meta:
        model = Corparation
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    parents = CorparationSerializer(source='parent',read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    parents = CompanySerializer(source='parent',read_only=True)
    class Meta:
        model = Factory
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    parents = FactorySerializer(source='parent',read_only=True)
    class Meta:
        model = Department
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    parents = DepartmentSerializer(source='parent',read_only=True)
    class Meta:
        model = Shift
        fields = '__all__'

class LunchSerializer(serializers.ModelSerializer):
    parents = ShiftSerializer(source='parent',read_only=True)
    class Meta:
        model = Lunch
        fields = '__all__'

class AgreagatSerializer(serializers.ModelSerializer):
    parents = DepartmentSerializer(source='parent',read_only=True)
    class Meta:
        model = Agreagat
        fields = '__all__'

class SensorsSerializer(serializers.ModelSerializer):
    parents = AgreagatSerializer(source='parent',read_only=True)
    class Meta:
        model = Sensors
        fields = '__all__'