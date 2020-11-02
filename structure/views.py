import json

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from structure.models import FirstObject, Shift, Department, Lunch


# @permission_classes([IsAuthenticated])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
class Parametrs(APIView):
    @api_view(('POST',))
    def step1(self):
        data = self.request.POST
        ob = FirstObject(name=data['name'],
                         customer=data['customer'],
                         contract=data['contract'],
                         structure=json.loads(data['structure'])
                         )
        ob.save()

    @api_view(('GET',))
    def get_structure(self):
        ob = FirstObject.objects.all().first()
        if ob:
            structure = {
                'name': ob['name'],
                'customer': ob['customer'],
                'contract': ob['contract'],
                'structure': ob['structure']
            }
        else:
            structure = {'result': 'empty'}
        return Response(structure)

    @api_view(('POST',))
    def create_shift(self):
        data = self.request.POST
        dep = Department(
            name=data['name'],
            factory_id=data['factory_id']
        )
        dep.save()
        k = 1
        shift = []
        for s in data['shifts']:
            shift[k] = Shift(
                name=str(k),
                dep_id=s['department_id'],
                start=s['start'],
                end=s['end']
            )
            shift[k].save()
            for l in s['lanch']:
                lunch = Lunch(
                    start=l['start'],
                    end=l['end']
                )
                lunch.save()
            k += 1
        return Response({'result': 'success'})
