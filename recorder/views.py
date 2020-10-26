from django.http import Http404
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
        id = self.request.query_params.get('id')
        if(id):

            try:
                Department.objects.get(pk=id)
                deps = [{
                    "id": dep.pk,
                    "name": dep.name,
                    "factory_name": dep.factory.name,
                    "corparation_name": dep.factory.corp.name
                } for dep in Department.objects.filter(pk=id)]
            except Department.DoesNotExist:
                raise Http404
        else:
            deps = [{
                "id": dep.pk,
                "name": dep.name,
                "factory_name": dep.factory.name,
                "corparation_name":dep.factory.corp.name
                    } for dep in Department.objects.all()]
        return Response(deps)
