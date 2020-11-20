import json

from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from project_v_0_0_1.settings import BASE_STRUCTURE
from structure.models import FirstObject, Shift, Department, Lunch
from .models import *
from .serializer import *


@permission_classes([IsAuthenticated])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
class Parametrs(APIView):
    """
    Класс для создание первичного объекта из выбра пользователя

     Methods
    ===========

    - step1 - POST - метод создает первичную структура организации из выбора пользователя
    - get_structure - GET - получаем первый созданный объект структуры
    - create_shift - POST - создает смены
    """
    @api_view(('POST',))
    def step1(self):
        """метод для создания первичной структуры"""
        data = self.data
        model_list = []
        for i in data['structure']:
            model_list.append(BASE_STRUCTURE[data['structure'][i]])
        ob = FirstObject(name=data['name'],
                         customer=data['customer'],
                         contract=data['contract'],
                         structure=json.dumps(data['structure']),
                         listModels=json.dumps(model_list)
                         )
        last_id = 0
        start_id = 0
        for s in BASE_STRUCTURE:
            if s in BASE_STRUCTURE[data['structure']['levlel_0']]:
                break
            a = globals()[s]()
            if last_id!=0:
                a.parent_id = last_id
            if s == 'Reserv_1':
                a.save(True)
            else:
                a.save(True)
            if last_id==0:
                start_id = a.id
            last_id = a.id
        ob.start_object = start_id
        ob.save()
        return Response({'data': 'success'})

    @api_view(('GET',))
    def get_structure(self):
        """получение структуры"""
        ob = FirstObject.objects.all().first()
        if ob:
            structure = {
                'name': ob.name,
                'customer': ob.customer,
                'contract': ob.contract,
                'structure': ob.structure
            }
        else:
            structure = {'result': 'empty'}
        return Response(structure)

    @api_view(('POST',))
    def create_shift(self):
        """метод созданиия цеха совместно со сменами и перерывами """
        data = self.data
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


@permission_classes([IsAuthenticated])
class Reserv2_Search(APIView):
    def get(self, request, pk):
        art = Reserv_2.objects.filter(res1=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = Reserv_2Serializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Corparation_Search(APIView):
    def get(self, request, pk):
        art = Corparation.objects.filter(res2=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CorparationSerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Company_Search(APIView):
    def get(self, request, pk):
        art = Company.objects.filter(corp=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CompanySerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Factory_Search(APIView):
    def get(self, request, pk):
        art = Factory.objects.filter(comp=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = FactorySerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Department_Search(APIView):
    def get(self, request, pk):
        art = Department.objects.filter(factory=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = DepartmentSerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Agreagat_Search(APIView):
    def get(self, request, pk):
        art = Agreagat.objects.filter(dep=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = AgreagatSerializer(art, many=True)
        return Response(serializer.data)
