from rest_framework import serializers

from recorder.models import Workspace, Workarea


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

class WorkareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workarea
        fields = '__all__'