from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from users.models import UserP
from datetime import datetime, timedelta
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



#виджет «Продолжительность работы, ч», вкладка день
@permission_classes([IsAuthenticated])
class DurationIntervalDayViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'DurationIntervalDay':
                    dash = d.name
        try:
            art = globals()[dash].objects.filter(date=date)
            sum = 0
            format = "%H:%M:%S"
            data1 =[]
            for i in art:
                duration = datetime.strptime(str(i.end), format)-datetime.strptime(str(i.start), format)
                duration = duration.total_seconds() / 3600
                k = {
                        "start":i.start,
                        "end":i.end,
                        "duration":duration
                }
                data1.append(k)
                sum = sum + duration
            data = {
                "interval": data1,
                "sum":sum
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Продолжительность работы, ч», вкладка смена
@permission_classes([IsAuthenticated])
class DurationIntervalShiftViews(APIView):
    pass

#виджет «Остатки на складах»
@permission_classes([IsAuthenticated])
class RemainderViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'RemainderStorehouse':
                    dash = d.name
        try:
            art = globals()[dash].objects.filter(date=date)
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Выпуск панелей» для вкладки «день»
@permission_classes([IsAuthenticated])
class EditionDayViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EditionDay':
                    dash = d.name
        try:
            art = globals()[dash].objects.get(date=date)
            delt = timedelta(days=1)
            date_del = date-delt
            art_del = globals()[dash].objects.get(date=date_del)
            print(EditionDay.objects.get(date=date))
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Выпуск панелей» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class EditionMonthViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EditionDay':
                    dash = d.name
        delt = timedelta(days=1)
        data_pred = date - timedelta(days=date.day)
        sh = date.day
        dat = date
        #текущий месяц
        suitable = 0
        substandard = 0
        defect = 0
        flooded = 0
        sum = 0
        try:
            while sh != 0:
                art = globals()[dash].objects.get(date=dat)
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
                try:
                    art = globals()[dash].objects.get(date=data_pred)
                except EditionDay.DoesNotExist:
                    a = Dashboard.objects.get(pk=2).tablename_set.all()
                    #
                    art = globals()[dash].objects.get(date=data_pred)
                suitable_pr = suitable_pr + art.suitable
                substandard_pr = substandard_pr + art.substandard
                defect_pr = defect_pr + art.defect
                flooded_pr = flooded_pr + art.flooded
                sum_pr = sum_pr + art.sum
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Выпуск панелей» для вкладки «смена»
@permission_classes([IsAuthenticated])
class EditionShiftViews(APIView):
    pass


#виджет «Суммарный расход» для вкладки «день»
@permission_classes([IsAuthenticated])
class SumexpenseDayViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'SumexpenseDay':
                    dash = d.name
        try:
            art = globals()[dash].objects.get(date=date)
            data = {
                "iso": art.iso,
                "pol": art.pol,
                "pen": art.pen,
                "kat1": art.kat1,
                "kat2": art.kat2,
                "kat3": art.kat3
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)


#виджет «Суммарный расход» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class SumexpenseMonthViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'SumexpenseDay':
                    dash = d.name
        sh = date.day
        dat = date
        delt = timedelta(days=1)
        iso = 0
        pol = 0
        pen = 0
        kat1 = 0
        kat2 = 0
        kat3 = 0
        try:
            while sh != 0:
                art = globals()[dash].objects.get(date=dat)
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Суммарный расход» для вкладки «смена»
@permission_classes([IsAuthenticated])
class SumexpenseShiftViews(APIView):
    pass

#виджет «Расход энергоресурсов» для вкладки «день»
@permission_classes([IsAuthenticated])
class EnergyConsumptionDayViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EnergyConsumptionDay':
                    dash = d.name
        try:
            art = globals()[dash].objects.get(date=date)
            data = {
                "input1": art.input1,
                "input2": art.input2,
                "gas": art.gas
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)

#виджет «Расход энергоресурсов» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class EnergyConsumptionMonthViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EnergyConsumptionDay':
                    dash = d.name
        try:
            sh = date.day
            dat = date
            delt = timedelta(days=1)
            input1 = 0
            input2 = 0
            gas = 0
            while sh != 0:
                art = globals()[dash].objects.get(date=dat)
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)



#виджет «Расход энергоресурсов» для вкладки «смена»
@permission_classes([IsAuthenticated])
class EnergyConsumptionShiftViews(APIView):
    pass


#виджет «Удельный расход на км» для вкладки «день»
@permission_classes([IsAuthenticated])
class SpecificConsumptionDayViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'SpecificConsumptionDay':
                    dash = d.name
        try:
            art = globals()[dash].objects.get(date=date)
            data = {
                "iso": art.iso,
                "pol": art.pol,
                "pen": art.pen,
                "kat1": art.kat1,
                "kat2": art.kat2,
                "kat3": art.kat3
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)


#виджет «Удельный расход на км» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class SpecificConsumptionMonthViews(APIView):
    def get(self, request, date):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'SpecificConsumptionDay':
                    dash = d.name
        sh = date.day
        dat = date
        delt = timedelta(days=1)
        iso = 0
        pol = 0
        pen = 0
        kat1 = 0
        kat2 = 0
        kat3 = 0
        try:
            while sh != 0:
                art = globals()[dash].objects.get(date=dat)
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
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)



#виджет «Удельный расход на км» для вкладки «смена»
@permission_classes([IsAuthenticated])
class SpecificConsumptionShiftViews(APIView):
    pass


#виджет «Модуль сравнения» для вкладки «день»
@permission_classes([IsAuthenticated])
class ComparisonDayViews(APIView):
    def get(self, request, date1, date2):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EditionDay':
                    dash = d.name
        try:
            art1 = globals()[dash].objects.get(date=date1)
            art2 = globals()[dash].objects.get(date=date2)
            data = {
                "suitable1": art1.suitable,
                "sui1_ch": ((art1.suitable / art2.suitable) - 1) * 100,
                "suitable2": art2.suitable,
                "substandard1": art1.substandard,
                "sub1_ch": ((art1.substandard / art2.substandard) - 1) * 100,
                "substandard2": art2.substandard,
                "defect1": art1.defect,
                "def1_ch": ((art1.defect / art2.defect) - 1) * 100,
                "defect2": art2.defect,
                "flooded1": art1.flooded,
                "flo_ch": ((art1.flooded / art2.flooded) - 1) * 100,
                "flooded2": art2.flooded,
                "sum1": art1.sum,
                "sum1_ch": ((art1.sum / art2.sum) - 1) * 100,
                "sum2": art2.sum
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)



#виджет «Модуль сравнения» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class ComparisonMonthViews(APIView):
    def get(self, request, date1, date2):
        role = UserP.objects.get(id=request.user.pk).role_set.all()
        for r in role:
            for d in r.dashboard.all():
                if d.name == 'EditionDay':
                    dash = d.name
        try:
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
                art = globals()[dash].objects.get(date=dat1)
                suitable1 = suitable1 + art.suitable
                substandard1 = substandard1 + art.substandard
                defect1 = defect1 + art.defect
                flooded1 = flooded1 + art.flooded
                sum1 = sum1 + art.sum
                dat1 = dat1 -delt
                sh1 = sh1 -1
            while sh2 != 0:
                art = globals()[dash].objects.get(date=dat2)
                suitable2 = suitable2 + art.suitable
                substandard2 = substandard2 + art.substandard
                defect2 = defect2 + art.defect
                flooded2 = flooded2 + art.flooded
                sum2 = sum2 + art.sum
                dat2 = dat2 -delt
                sh2 = sh2 -1
            data = {
                "suitable1": suitable1,
                "sui1_ch": ((suitable1/suitable2)-1)*100,
                "suitable2": suitable2,
                "substandard1": substandard1,
                "sub1_ch": ((substandard1 / substandard2) - 1) * 100,
                "substandard2": substandard2,
                "defect1": defect1,
                "def1_ch": ((defect1 / defect2) - 1) * 100,
                "defect2": defect2,
                "flooded1": flooded1,
                "flo_ch": ((flooded1 / flooded2) - 1) * 100,
                "flooded2": flooded2,
                "sum1": sum1,
                "sum1_ch": ((sum1 / sum2) - 1) * 100,
                "sum2": sum2
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)


#виджет «Модуль сравнения» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class ComparisonShiftViews(APIView):
    pass