from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from recorder.models import Workspace, Workarea, ValueSensor, WorkareaData
from structure.serializer import SensorsSerializer


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'


class WorkareaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkareaData
        fields = "__all__"
        extra_kwargs = {
             "workarea": {"required": False},
             "value": {"required": False},
        }

class ValueSensorSerializer(serializers.ModelSerializer):
    sensor = SensorsSerializer(read_only=True)
    class Meta:
        model = ValueSensor
        fields = '__all__'


class WorkareaSerializer(serializers.ModelSerializer):
    data = WorkareaDataSerializer(many=True)
    child = WorkareaDataSerializer(source='workareadata_set.all', read_only=True, many=True)
    class Meta:
        model = Workarea
        fields = '__all__'
        extra_kwargs = {
            "parent": {"required": False},
        }

    def create(self, validated_data):
        data_data = validated_data.pop('data')
        area_data = Workarea.objects.create(**validated_data)
        for d in data_data:
            WorkareaData.objects.create(workarea=area_data, **d)
        return area_data

    def update(self, instance, validated_data):
        data_data = validated_data.pop('data')
        WorkareaData.objects.filter(workarea=instance).delete()
        for d in data_data:
            WorkareaData.objects.create(workarea=instance, **d)
        instance = super(WorkareaSerializer, self).update(instance, validated_data)
        return instance