from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from structure.models import Department


@permission_classes([IsAuthenticated])
class Recorder(APIView):
    def get(self, request, format=None):
        deps = [dep.name for dep.name in Department.objects.all()]
        return Response(deps)
