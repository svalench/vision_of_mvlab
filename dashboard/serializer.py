from .models import *
from rest_framework import serializers

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'

# class DateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Date
#         fields = '__all__'

class DurationIntervalDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DurationIntervalDay
        fields = '__all__'

# class RemainderStorehouseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RemainderStorehouse
#         fields = '__all__'
#
# class RemainderIsoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RemainderIso
#         fields = '__all__'
#
# class RemainderPolSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RemainderPol
#         fields = '__all__'

# class RemainderPenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RemainderPen
#         fields = '__all__'

class EditionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EditionDay
        fields = '__all__'

class SumexpenseDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SumexpenseDay
        fields = '__all__'

class EnergyConsumptionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyConsumptionDay
        fields = '__all__'

class SpecificConsumptionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificConsumptionDay
        fields = '__all__'
