from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import json
from datetime import datetime, timedelta

# class DashboardViews(APIView):
#     def get(self, request):
#         art = Dashboard.objects.all()
#         # the many param informs the serializer that it will be serializing more than a single article.
#         serializer = DashboardSerializer(art, many=True)
#         return Response(serializer.data)
#
# class DateViews(APIView):
#     def get(self, request):
#         art = Date.objects.all()
#         # the many param informs the serializer that it will be serializing more than a single article.
#         serializer = DateSerializer(art, many=True)
#         return Response(serializer.data)


class DurationIntervalDayViews(APIView):
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

class EditionDayViews(APIView):
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


class EditionMonthViews(APIView):
    def get(self, request, date):
        delt = timedelta(days=1)
        # date_del = date-delt
        data_pred = date - timedelta(days=date.day)
        sh = date.day
        dat = date
        #текущий месяц
        suitable = 0
        substandard = 0
        defect = 0
        flooded = 0
        sum = 0
        while sh != 0:
            dateb = Date.objects.get(date=dat)
            art = EditionDay.objects.get(date=dateb.id)
            suitable = suitable + art.suitable
            substandard = substandard + art.suitable
            defect = defect + art.defect
            flooded = flooded + art.flooded
            sum = sum + art.sum
            dat = dat - delt
            sh = sh - 1
        sh = data_pred.day


        #пред. месяц
        suitable_pr = 0
        substandard_pr = 0
        defect_pr = 0
        flooded_pr = 0
        sum_pr = 0
        while sh != 0:
            dateb = Date.objects.get(date=data_pred)
            art = EditionDay.objects.get(date=dateb.id)
            suitable_pr = suitable_pr + art.suitable
            substandard_pr = substandard_pr + art.substandard
            defect_pr = defect_pr + art.defect
            flooded_pr = flooded_pr + art.flooded
            sum_pr = sum_pr + art.sum_pr
            data_pred = data_pred - delt
            sh = sh - 1
        data = {
            "suitable": suitable,
            "change_suitable": (((suitable/suitable_pr)-1)*100),
            "substandard": substandard,
            "change_substandard": (((substandard/substandard_pr)-1)*100),
            "defect": defect,
            "change_defect": (((defect/defect_pr)-1)*100),
            "flooded": flooded,
            "change_flooded": (((flooded/flooded_pr)-1)*100),
            "sum": sum,
            "change_sum": (((sum/sum_pr)-1)*100)
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


class SumexpenseMonthViews(APIView):
    def get(self, request, date):
        sh = date.day
        dat = date
        delt = timedelta(days=1)
        iso = 0
        pol = 0
        pen = 0
        kat1 = 0
        kat2 = 0
        kat3 = 0
        while sh != 0:
            dateb = Date.objects.get(date=dat)
            art = SumexpenseDay.objects.get(date=dateb.id)
            iso = iso + art.iso
            pol = pol + art.pol
            pen = pen + art.pen
            kat1 = kat1 + art.kat1
            kat2 = kat2 + art.kat2
            kat3 = kat3 + art.kat3
            dat = dat - delt
            sh = sh - 1
        data = {
            "iso": iso,
            "pol": pol,
            "pen": pen,
            "kat1": kat1,
            "kat2": kat2,
            "kat3": kat3
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


class EnergyConsumptionMonthViews(APIView):
    def get(self, request, date):
        sh = date.day
        dat = date
        delt = timedelta(days=1)
        input1 = 0
        input2 = 0
        gas = 0
        while sh != 0:
            dateb = Date.objects.get(date=dat)
            art = EnergyConsumptionDay.objects.get(date=dateb.id)
            input1 = input1 + art.input1
            input2 = input2 + art.input2
            gas = gas + art.gas
            dat = dat -delt
            sh = sh -1
        data = {
            "input1": input1,
            "input2": input2,
            "gas": gas
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

class SpecificConsumptionMonthViews(APIView):
    def get(self, request, date):
        sh = date.day
        dat = date
        delt = timedelta(days=1)
        iso = 0
        pol = 0
        pen = 0
        kat1 = 0
        kat2 = 0
        kat3 = 0
        while sh != 0:
            dateb = Date.objects.get(date=dat)
            art = SpecificConsumptionDay.objects.get(date=dateb.id)
            iso = iso + art.iso
            pol = pol + art.pol
            pen = pen + art.pen
            kat1 = kat1 + art.kat1
            kat2 = kat2 + art.kat2
            kat3 = kat3 + art.kat3
            dat = dat -delt
            sh = sh -1
        data = {
            "iso": iso,
            "pol": pol,
            "pen": pen,
            "kat1": kat1,
            "kat2": kat2,
            "kat3": kat3
        }
        return Response(data)

class ComparisonDayViews(APIView):
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


class ComparisonMonthViews(APIView):
    def get(self, request, date1, date2):
        sh1 = date1.day
        dat1 = date1
        sh2 = date2.day
        dat2 = date2
        delt = timedelta(days=1)
        suitable1 = 0
        suitable2 = 0
        substandard1 = 0
        substandard2 = 0
        defect1 = 0
        defect2 = 0
        flooded1 = 0
        flooded2 = 0
        sum1 = 0
        sum2 = 0
        while sh1 != 0:
            dateb = Date.objects.get(date=dat1)
            art = EditionDay.objects.get(date=dateb.id)
            suitable1 = suitable1 + art.suitable
            substandard1 = substandard1 + art.substandard
            defect1 = defect1 + art.defect
            flooded1 = flooded1 + art.flooded
            sum1 = sum1 + art.sum
            dat1 = dat1 -delt
            sh1 = sh1 -1
        while sh2 != 0:
            dateb = Date.objects.get(date=dat2)
            art = EditionDay.objects.get(date=dateb.id)
            suitable2 = suitable2 + art.suitable
            substandard2 = substandard2 + art.substandard
            defect2 = defect2 + art.defect
            flooded2 = flooded2 + art.flooded
            sum2 = sum2 + art.sum
            dat2 = dat2 -delt
            sh2 = sh2 -1
        data = {
            "suitable1": suitable1,
            "suitable2": suitable2,
            "substandard1": substandard1,
            "substandard2": substandard2,
            "defect1": defect1,
            "defect2": defect2,
            "flooded1": flooded1,
            "flooded2": flooded2,
            "sum1": sum1,
            "sum2": sum2
        }
        return Response(data)