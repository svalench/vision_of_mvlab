from rest_framework import serializers

from recorder.models import Workspace, Workarea, ValueSensor


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

class WorkareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workarea
        fields = '__all__'

class ValueSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueSensor
        fields = '__all__'