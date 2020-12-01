from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from users.models import UserP
from datetime import datetime, timedelta
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# from django.db import connection



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
                if d.name == 'Storehouse':
                    dash = d.name
        try:
            art = globals()[dash].objects.all()
            storehouse = []
            isosum =0
            polsum = 0
            pensum = 0
            for a in art:
                iso = []
                pen = []
                pol = []
                for i in a.substance_set.filter(short_name='ISO'):
                    iso.append(i.value_date(date))
                    isosum =isosum + i.value_date(date)
                for i in a.substance_set.filter(short_name='PEN'):
                    pen.append(i.value_date(date))
                    pensum = pensum + i.value_date(date)
                for i in a.substance_set.filter(short_name='POL'):
                    pol.append(i.value_date(date))
                    polsum = polsum + i.value_date(date)
                data = {
                    "name": a.name,
                    "iso": iso,
                    "pol": pol,
                    "pen": pen,
                }
                storehouse.append(data)
            data = {
                "storehouse": storehouse,
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
            if globals()[dash].objects.filter(date=date).exists():
                art = globals()[dash].objects.get(date=date)
            else:
                calculate_edition(date)
                art = globals()[dash].objects.get(date=date)
            delt = timedelta(days=1)
            date_del = date-delt
            if globals()[dash].objects.filter(date=date_del).exists():
                art_del = globals()[dash].objects.get(date=date_del)
            else:
                calculate_edition(date_del)
                art_del = globals()[dash].objects.get(date=date_del)
            if art_del.suitable != 0:
                change_suitable = (((art.suitable/art_del.suitable)-1)*100)
                print('11')
            else:
                print('222')
                change_suitable = 0
            if art_del.substandard != 0:
                change_substandard = (((art.substandard/art_del.substandard)-1)*100)
            else:
                change_substandard = 0
            if art_del.defect != 0:
                change_defect = (((art.defect/art_del.defect)-1)*100)
            else:
                change_defect = 0
            if art_del.flooded != 0:
                change_flooded = (((art.flooded/art_del.flooded)-1)*100)
            else:
                change_flooded = 0
            if art_del.sum != 0:
                change_sum = (((art.sum/art_del.sum)-1)*100)
            else:
                change_sum = 0
            data = {
                "suitable": art.suitable,
                "change_suitable": change_suitable,
                "substandard": art.substandard,
                "change_substandard": change_substandard,
                "defect": art.defect,
                "change_defect": change_defect,
                "flooded": art.flooded,
                "change_flooded": change_flooded,
                "sum": art.sum,
                "change_sum": change_sum
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
                if globals()[dash].objects.filter(date=dat).exists():
                    art = globals()[dash].objects.get(date=dat)
                else:
                    art = calculate_edition(dat)
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
                if globals()[dash].objects.filter(date=data_pred).exists():
                    art = globals()[dash].objects.get(date=data_pred)
                else:
                    art = calculate_edition(data_pred)
                suitable_pr = suitable_pr + art.suitable
                substandard_pr = substandard_pr + art.substandard
                defect_pr = defect_pr + art.defect
                flooded_pr = flooded_pr + art.flooded
                sum_pr = sum_pr + art.sum
                data_pred = data_pred - delt
                sh = sh - 1

            if suitable_pr != 0:
                change_suitable = (((suitable/suitable_pr)-1)*100)
            else:
                change_suitable = 0
            if substandard_pr != 0:
                change_substandard = (((substandard/substandard_pr)-1)*100)
            else:
                change_substandard = 0
            if defect_pr != 0:
                change_defect = (((defect/defect_pr)-1)*100)
            else:
                change_defect = 0
            if flooded_pr != 0:
                change_flooded = (((flooded/flooded_pr)-1)*100)
            else:
                change_flooded = 0
            if sum_pr != 0:
                change_sum = (((sum/sum_pr)-1)*100)
            else:
                change_sum = 0
            data = {
                "suitable": suitable,
                "change_suitable": change_suitable,
                "substandard": substandard,
                "change_substandard": change_substandard,
                "defect": defect,
                "change_defect": change_defect,
                "flooded": flooded,
                "change_flooded": change_flooded,
                "sum": sum,
                "change_sum": change_sum
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
            if globals()[dash].objects.filter(date=date).exists():
                art = globals()[dash].objects.get(date=date)
            else:
                art = calculate_sumexpense(date)
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
                if globals()[dash].objects.filter(date=dat).exists():
                    art = globals()[dash].objects.get(date=dat)
                else:
                    art = calculate_sumexpense(dat)
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
            if globals()[dash].objects.filter(date=date).exists():
                art = globals()[dash].objects.get(date=date)
            else:
                art = calculate_energy_consumption(date)
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
                if globals()[dash].objects.filter(date=dat).exists():
                    art = globals()[dash].objects.get(date=dat)
                else:
                    art = calculate_energy_consumption(dat)
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
            if globals()[dash].objects.filter(date=date).exists():
                art = globals()[dash].objects.get(date=date)
            else:
                art = calculate_specific(date)
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
                if globals()[dash].objects.filter(date=dat).exists():
                    art = globals()[dash].objects.get(date=dat)
                else:
                    art = calculate_specific(dat)
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
            if globals()[dash].objects.filter(date=date1).exists():
                art1 = globals()[dash].objects.get(date=date1)
            else:
                art1 = calculate_edition(date1)
                # art1 = globals()[dash].objects.get(date=date1)
            if globals()[dash].objects.filter(date=date2).exists():
                art2 = globals()[dash].objects.get(date=date2)
            else:
                art2 = calculate_edition(date2)
                # art2 = globals()[dash].objects.get(date=date2)
            if art2.suitable != 0:
                change_suitable = (((art1.suitable/art2.suitable)-1)*100)
            else:
                change_suitable = 0
            if art2.substandard != 0:
                change_substandard = (((art1.substandard/art2.substandard)-1)*100)
            else:
                change_substandard = 0
            if art2.defect != 0:
                change_defect = (((art1.defect/art2.defect)-1)*100)
            else:
                change_defect = 0
            if art2.flooded != 0:
                change_flooded = (((art1.flooded/art2.flooded)-1)*100)
            else:
                change_flooded = 0
            if art2.sum != 0:
                change_sum = (((art1.sum/art2.sum)-1)*100)
            else:
                change_sum = 0

            data = {
                "suitable1": art1.suitable,
                "sui1_ch": change_suitable,
                "suitable2": art2.suitable,
                "substandard1": art1.substandard,
                "sub1_ch": change_substandard,
                "substandard2": art2.substandard,
                "defect1": art1.defect,
                "def1_ch": change_defect,
                "defect2": art2.defect,
                "flooded1": art1.flooded,
                "flo_ch": change_flooded,
                "flooded2": art2.flooded,
                "sum1": art1.sum,
                "sum1_ch": change_sum,
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
                if globals()[dash].objects.filter(date=dat1).exists():
                    art = globals()[dash].objects.get(date=dat1)
                else:
                    art = calculate_edition(dat1)
                suitable1 = suitable1 + art.suitable
                substandard1 = substandard1 + art.substandard
                defect1 = defect1 + art.defect
                flooded1 = flooded1 + art.flooded
                sum1 = sum1 + art.sum
                dat1 = dat1 -delt
                sh1 = sh1 -1
            while sh2 != 0:
                if globals()[dash].objects.filter(date=dat2).exists():
                    art = globals()[dash].objects.get(date=dat2)
                else:
                    art = calculate_edition(dat2)
                suitable2 = suitable2 + art.suitable
                substandard2 = substandard2 + art.substandard
                defect2 = defect2 + art.defect
                flooded2 = flooded2 + art.flooded
                sum2 = sum2 + art.sum
                dat2 = dat2 -delt
                sh2 = sh2 -1
                if suitable2 != 0:
                    sui1_ch = ((suitable1/suitable2)-1)*100
                else:
                    sui1_ch = 0
                if substandard2 != 0:
                    sub1_ch = ((substandard1/substandard2)-1)*100
                else:
                    sub1_ch = 0
                if defect2 != 0:
                    def1_ch = ((defect1 / defect2) - 1) * 100
                else:
                    def1_ch = 0
                if flooded2 != 0:
                    flo_ch = ((flooded1 / flooded2) - 1) * 100
                else:
                    flo_ch = 0
                if sum2 != 0:
                    sum1_ch = ((sum1 / sum2) - 1) * 100
                else:
                    sum1_ch = 0
            data = {
                "suitable1": suitable1,
                "sui1_ch": sui1_ch,
                "suitable2": suitable2,
                "substandard1": substandard1,
                "sub1_ch": sub1_ch,
                "substandard2": substandard2,
                "defect1": defect1,
                "def1_ch": def1_ch,
                "defect2": defect2,
                "flooded1": flooded1,
                "flo_ch": flo_ch,
                "flooded2": flooded2,
                "sum1": sum1,
                "sum1_ch": sum1_ch,
                "sum2": sum2
            }
        except UnboundLocalError:
            data = 'not Role'
        return Response(data)


#виджет «Модуль сравнения» для вкладки «месяц»
@permission_classes([IsAuthenticated])
class ComparisonShiftViews(APIView):
    pass