from django.forms import model_to_dict
from django.http import Http404
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recorder.models import Workarea, ValueSensor
from structure.models import Department, Agreagat


@permission_classes([IsAuthenticated])
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


class ChartData(APIView):
    """класс для вывода графиков по рабочим областям"""
    def get(self, format=None):
        id = self.request.query_params.get('id')
        keys = self.request.query_params.get('key', None)
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if(id):
            try:
                area = Workarea.objects.get(pk=id)
            except Workarea.DoesNotExist:
                raise ValidationError("Not Found Workarea with pk %s"%id)
            result = {key: value for key,value in model_to_dict(area).items() if key!='data'}
            a = self.__choice_method(area=area, keys=keys, start=start, end=end)
            result['child'] = a
            return Response(result)
        else:
            raise Http404

    def __choice_method(self, area, keys=None, start=None, end=None):
        """метод для выбора вывода данных за период по фильтру"""
        a = []
        for l in area.workareadata_set.all():
            res = {key: value for key, value in model_to_dict(l).items()}
            res['sensor_data'] = model_to_dict(ValueSensor.objects.get(pk=l.value.id))
            if keys != None:
                if (keys == "hour"):
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_last_hour()
                elif (keys == "day"):
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_last_day()
                elif (keys == "week"):
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_last_week()
                elif (keys == "month"):
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_last_month()
                else:
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_last_shift()
            else:
                if start is not None and end is not None:
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_mode_by_periods_interval(start=start, end=end)
                else:
                    res['values'] = ValueSensor.objects.get(pk=l.value.id).get_period(start=start, end=end)
            a.append(res)
        return a
