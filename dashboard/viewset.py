from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import json
from datetime import datetime, timedelta

class DashboardViews(APIView):
    def get(self, request):
        art = Dashboard.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = DashboardSerializer(art, many=True)
        return Response(serializer.data)

class DateViews(APIView):
    def get(self, request):
        art = Date.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = DateSerializer(art, many=True)
        return Response(serializer.data)

class DurationViews(APIView):
    def get(self, request, date):
        dateb = Date.objects.get(date=date)
        art = DurationIntervalDay.objects.filter(date=dateb.id)
        DurationIntervalDayS = DurationIntervalDaySerializer(art, many=True)
        sum = 0
        format = "%H:%M:%S"
        data1 =[]
        for i in range(len(DurationIntervalDayS.data)):
            start = datetime.strptime(DurationIntervalDayS.data[i]["start"], format)
            end = datetime.strptime(DurationIntervalDayS.data[i]["end"], format)
            duration = (end - start).total_seconds()/3600
            k={
                "start":DurationIntervalDayS.data[i]["start"],
                "end":DurationIntervalDayS.data[i]["end"],
                "duration":duration
            }
            data1.append(k)
            sum = sum + duration
        data = {
            "interval": data1,
            "sum":sum
        }
        # json_string = json.dumps(data)
        return Response(data)

class RemainderViews(APIView):
    def get(self, request, date):
        dateb = Date.objects.get(date=date)
        art = RemainderStorehouse.objects.filter(date=dateb.id)
        storehouse = []
        isosum = 0
        polsum = 0
        pensum = 0
        for i in art:
            diso = RemainderIso.objects.filter(storehouse=i.id)
            dpol = RemainderPol.objects.filter(storehouse=i.id)
            dpen = RemainderPen.objects.filter(storehouse=i.id)
            dataiso = []
            datapol = []
            datapen = []
            for j in diso:
                dataiso.append(j.quantity)
                isosum = isosum + j.quantity
            for j in dpol:
                datapol.append(j.quantity)
                polsum = polsum + j.quantity
            for j in dpen:
                datapen.append(j.quantity)
                pensum = pensum + j.quantity
            stor = {
                "name": i.name,
                "iso": dataiso,
                "pol": datapol,
                "pen": datapen
            }
            storehouse.append(stor)
        data = {
            "storehouse":storehouse,
            "in_total": {
                "iso": isosum,
                "pol": polsum,
                "pen": pensum
            }
        }
        return Response(data)

class EditionViews(APIView):
    def get(self, request, date):
        delt = timedelta(days=1)
        date_del = date-delt
        dateb = Date.objects.get(date=date)
        dateb_del = Date.objects.get(date=date_del)
        art_del = EditionDay.objects.get(date=dateb_del.id)
        art = EditionDay.objects.get(date=dateb.id)
        data = {
            "suitable": art.suitable,
            "change_suitable": (((art.suitable/art_del.suitable)-1)*100),
            "substandard": art.substandard,
            "change_substandard": (((art.substandard/art_del.substandard)-1)*100),
            "defect": art.defect,
            "change_defect": (((art.defect/art_del.defect)-1)*100),
            "flooded": art.flooded,
            "change_flooded": (((art.flooded/art_del.flooded)-1)*100),
            "sum": art.sum,
            "change_sum": (((art.sum/art_del.sum)-1)*100)
        }
        return Response(data)

class SumexpenseDayViews(APIView):
    def get(self, request, date):
        dateb = Date.objects.get(date=date)
        art = SumexpenseDay.objects.get(date=dateb.id)
        data = {
            "iso": art.iso,
            "pol": art.pol,
            "pen": art.pen,
            "kat1": art.kat1,
            "kat2": art.kat2,
            "kat3": art.kat3
        }
        return Response(data)

class EnergyConsumptionDayViews(APIView):
    def get(self, request, date):
        dateb = Date.objects.get(date=date)
        art = EnergyConsumptionDay.objects.get(date=dateb.id)
        data = {
            "input1": art.input1,
            "input2": art.input2,
            "gas": art.gas
        }
        return Response(data)

class SpecificConsumptionDayViews(APIView):
    def get(self, request, date):
        dateb = Date.objects.get(date=date)
        art = SpecificConsumptionDay.objects.get(date=dateb.id)
        data = {
            "iso": art.iso,
            "pol": art.pol,
            "pen": art.pen,
            "kat1": art.kat1,
            "kat2": art.kat2,
            "kat3": art.kat3
        }
        return Response(data)

class ComparisonViews(APIView):
    def get(self, request, date1, date2):
        dateb1 = Date.objects.get(date=date1)
        dateb2 = Date.objects.get(date=date2)
        art1 = EditionDay.objects.get(date=dateb1.id)
        art2 = EditionDay.objects.get(date=dateb2.id)
        data = {
            "suitable1": art1.suitable,
            "suitable2": art2.suitable,
            "substandard1": art1.substandard,
            "substandard2": art2.substandard,
            "defect1": art1.defect,
            "defect2": art2.defect,
            "flooded1": art1.flooded,
            "flooded2": art2.flooded,
            "sum1": art1.sum,
            "sum2": art2.sum
        }
        return Response(data)