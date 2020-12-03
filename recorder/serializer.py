from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from recorder.models import Workspace, Workarea, ValueSensor, WorkareaData
from structure.serializer import SensorsSerializer




class WorkareaDataSerializer(serializers.ModelSerializer):
    """класс сериализации для модели WorkareaData"""
    class Meta:
        model = WorkareaData
        fields = "__all__"
        extra_kwargs = {
             "workarea": {"required": False},
             "value": {"required": False},
        }

class ValueSensorSerializer(serializers.ModelSerializer):
    """ класс для сериализации модели ValueSensor

    Attributes
    ==========

    - sensor - связи к связанной модели SensorsSerializer

    """
    sensor_data = SensorsSerializer(read_only=True)
    class Meta:
        model = ValueSensor
        fields = '__all__'

class WorkareaSerializer(serializers.ModelSerializer):
    """модель сериализации данных для рабочей области

     Attributes
    =======

    - data - связи MtM к модели ValueSensorSerializer
    - child - получение данных из промежуточной модели MtM

    """
    data = WorkareaDataSerializer(many=True)
    child = WorkareaDataSerializer(source='workareadata_set.all', read_only=True, many=True)
    class Meta:
        model = Workarea
        fields = '__all__'
        extra_kwargs = {
            "parent": {"required": False},
        }

    def create(self, validated_data):
        """метод сохранения рабочей области с автоматическим добавлением MtM таблицы с кастомными полями"""
        # получаем данные о выбранном графике(оф)
        data_data = validated_data.pop('data')
        # создаем рабочую область
        area_data = Workarea.objects.create(**validated_data)
        # создаем связи к графикам
        for d in data_data:
            WorkareaData.objects.create(workarea=area_data, **d)
        return area_data

    def update(self, instance, validated_data):
        # получаем данные о выбранном графике(оф)
        data_data = validated_data.pop('data')
        # удаляем старые свяли
        WorkareaData.objects.filter(workarea=instance).delete()
        # создаем связи к графикам
        for d in data_data:
            WorkareaData.objects.create(workarea=instance, **d)
        # обновляем запись
        instance = super(WorkareaSerializer, self).update(instance, validated_data)
        return instance

class WorkspaceSerializer(serializers.ModelSerializer):
    child = WorkareaDataSerializer(source='workarea_set.all', read_only=True, many=True)
    """класс сериализации для модели Workspace"""
    class Meta:
        model = Workspace
        fields = '__all__'