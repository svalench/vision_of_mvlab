from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .models import *

from .serializer import *

#@permission_classes([IsAdminUser])
class CorparationView(viewsets.ModelViewSet):
    queryset = Corparation.objects.all()
    serializer_class = CorparationSerializer

#@permission_classes([IsAdminUser])
class FactoryView(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

#@permission_classes([IsAdminUser])
class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

#@permission_classes([IsAdminUser])
class ShiftView(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

#@permission_classes([IsAdminUser])
class LunchView(viewsets.ModelViewSet):
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer

#@permission_classes([IsAdminUser])
class AgreagatView(viewsets.ModelViewSet):
    queryset = Agreagat.objects.all()
    serializer_class = AgreagatSerializer

#@permission_classes([IsAdminUser])
class SensorsView(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

