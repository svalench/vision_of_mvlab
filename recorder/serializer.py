from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from recorder.models import Workspace, Workarea, ValueSensor, WorkareaData
from structure.serializer import SensorsSerializer, Sensors


class ValueSensorSerializer(serializers.ModelSerializer):
    """ класс для сериализации модели ValueSensor

    Attributes
    ==========

    - sensor - связи к связанной модели SensorsSerializer
    - data_sensor_data - test

    """
    parents = SensorsSerializer(source='sensor', read_only=True)
    sensor_name = serializers.SerializerMethodField('get_sensor_name')
    uzel_name = serializers.SerializerMethodField('get_uzel_name')
    department_name = serializers.SerializerMethodField('get_dep_name')
    factory_name = serializers.SerializerMethodField('get_factory_name')

    def get_sensor_name(self, a):
        """передает название сенсора"""
        return a.sensor.name

    def get_dep_name(self, a):
        """передает название департамента"""
        return a.sensor.parent.parent.name

    def get_uzel_name(self, a):
        """передает название узла"""
        return a.sensor.parent.name

    def get_factory_name(self, a):
        """передает название завода"""
        return a.sensor.parent.parent.parent.name

    class Meta:
        model = ValueSensor
        fields = '__all__'
        extra_kwargs = {
            "parent": {"required": False},
        }


class WorkareaDataSerializer(serializers.ModelSerializer):
    """класс сериализации для модели WorkareaData"""
    sensors_data = ValueSensorSerializer(source='value', read_only=True)

    class Meta:
        model = WorkareaData
        fields = "__all__"
        extra_kwargs = {
             "workarea": {"required": False},
             "value": {"required": False},
        }


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
    """класс сериализация для модели Workspace"""
    child = WorkareaDataSerializer(source='workarea_set.all', read_only=True, many=True)
    workares = serializers.SerializerMethodField('get_workareas')

    def get_workareas(self, a):
        """передает название сенсора"""
        return [{"id":i.id,"name":i.name} for i in a.workarea_set.all()]

    class Meta:
        model = Workspace
        fields = '__all__'