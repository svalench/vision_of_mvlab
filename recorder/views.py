from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from structure.models import Department, Agreagat


#@permission_classes([IsAuthenticated])
class Recorder(APIView):
    def get(self, request, format=None):
        id = self.request.query_params.get('id')
        if(id):

            try:
                Department.objects.get(pk=id)
                deps = [{
                    "id": agr.pk,
                    "name": agr.name,
                    "department_name":agr.parent.name,
                    "factory_name": agr.parent.parent.name,
                    "corparation_name": agr.parent.parent.parent.name,
                    'list_point':[{'sensor_id':p.pk,
                                   'sensor_name':p.name,
                                   "designation":p.designation,
                                   'values':[{
                                                    'id':v.pk,
                                                    'name':v.name,
                                                    'table_name':v.table_name,
                                                    'name_connection':v.name_connection
                                                } for v in p.valuesensor_set.all()],
                                   } for p in agr.sensors_set.all()]
                } for agr in Agreagat.objects.filter(pk=id)]
            except Department.DoesNotExist:
                raise Http404
        else:
            deps = [{
                "id": agr.pk,
                "name": agr.name,
                "department_name": agr.parent.name,
                "factory_name": agr.parent.name,
                "corparation_name":agr.parent.parent.name
                    } for agr in Agreagat.objects.all()]
        return Response(deps)
