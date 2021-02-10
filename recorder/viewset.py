from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError

from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

@permission_classes([IsAuthenticated])
class WorkspaceView(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        """ переопределяем запрос к модели с условием"""
        return Workspace.objects.filter(parent_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        request.data['parent'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        request.data['parent'] = request.user.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class ValueSensorView(viewsets.ModelViewSet):
    queryset = ValueSensor.objects.all()
    serializer_class = ValueSensorSerializer


@permission_classes([IsAuthenticated])
class WorkareaView(viewsets.ModelViewSet):
    queryset = Workarea.objects.all()
    serializer_class = WorkareaSerializer

    def get_queryset(self):
        queryset = Workarea.objects.all()
        parent = self.request.query_params.get('parent', None)
        if parent is not None:
            queryset = queryset.filter(parent_id=parent)
        return queryset

@permission_classes([IsAuthenticated])
class WorkareaDataView(viewsets.ModelViewSet):
    queryset = WorkareaData.objects.all()
    serializer_class = WorkareaDataSerializer


