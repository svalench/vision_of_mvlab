import json

from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from project_v_0_0_1.settings import BASE_STRUCTURE, SOCKET_PORT_SEREVER
from structure.models import FirstObject, Shift, Department, Lunch
from .models import *
from .serializer import *

import json
import socket


def send_status_to_server():
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect(('localhost', SOCKET_PORT_SEREVER))
        data = {"data": 1}
        print(data)
        data = json.dumps(data).encode('utf-8')
    except:
        return {"error": "no connection to socket"}
    try:
        sock.send(data)
    except:
        sock.close()
    try:
        res = sock.recv(1024)
    except:
        return {"error": "no connection to socket"}
    print(res)
    sock.close()
    return json.loads(res)


@permission_classes([IsAuthenticated])
class StatusConnections(APIView):
    def get(self, request):
        res = send_status_to_server()
        return Response(res)


def find_parent_id(prentid):
    ob = FirstObject.objects.all().first()
    structure = ob.listModels
    if 'Department' in structure:
        ind_struct = structure.index('Department')
        parent_name = structure[ind_struct-1]
        ind = BASE_STRUCTURE.index('Department')
        ind_parent = BASE_STRUCTURE.index(parent_name)
        counter = ind - ind_parent
        a = globals()[parent_name].objects.get(pk=prentid)
        print(a.child_model())
        c = list(a.child_model())[0]
        for i in range(counter):
            try:
                c = list(c.child_model())[0]
            except:
                continue
        print(c)
        return c.id
    else:
        return prentid

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
        ob.save()
        for s in BASE_STRUCTURE:
            if s in BASE_STRUCTURE[data['structure']['levlel_0']]:
                break
            a = globals()[s]()
            if last_id != 0:
                a.parent_id = last_id
            if s == 'Reserv_1':
                a.save(True)
            else:
                a.save(True)
            if last_id == 0:
                start_id = a.id
            last_id = a.id
        ob.start_object = start_id
        ob.save()
        return Response({'data': 'success'}, status=201)

    @api_view(('GET',))
    def get_structure(self):
        """получение структуры"""
        ob = FirstObject.objects.all().first()
        if ob:
            structure = {
                'name': ob.name,
                'customer': ob.customer,
                'contract': ob.contract,
                'structure': ob.structure,
                'date_add': ob.date_add,
                'date_update': ob.date_update

            }
        else:
            structure = {'result': 'empty'}
        return Response(structure)

    @api_view(('DELETE',))
    def delete_structure(self):
        """удаление структуры"""
        ob = FirstObject.objects.all().first()
        ob.delete()
        structure = {'result': 'structure %s delete' % ob.id}
        return Response(structure)




    @api_view(('POST',))
    def create_shift(self):
        """метод созданиия цеха совместно со сменами и перерывами """
        data = self.data
        data['parent'] = find_parent_id(data['parent'])
        dep = Department(
            name=data['name'],
            parent_id=data['parent']
        )
        dep.save()
        k = 0
        shift = []
        for s in data['shifts']:
            shift.append(Shift(
                name=str(k),
                parent_id=dep.id,
                start=s['start'],
                end=s['end']
            ))
            shift[k].save()
            for l in s['lanch']:
                lunch = Lunch(
                    parent_id=shift[k].id,
                    start=l['start'],
                    end=l['end']
                )
                lunch.save()
            k += 1
        res = DepartmentShiftsSerializer(dep)
        return Response(res.data, status=201)

    @api_view(('PUT',))
    def update_shift(request, pk):
        data = request.data
        print(pk)
        dep = Department.objects.get(id=pk)
        dep.parent_id = data['parent']
        dep.name = data['name']
        dep.save()
        for shift in data['shifts']:
            if "id" in shift:
                sh = Shift.objects.get(id=shift['id'])
                sh.start = shift['start']
                sh.end = shift['end']
                sh.save()
            else:
                sh = Shift(start=shift['start'],end=shift['end'], parent_id=pk)
                sh.save()
            if 'lanch' in shift:
                creat_or_udate_lunch(sh, shift['lanch'])
        print(data)
        dep = Department.objects.get(id=pk)
        res = DepartmentShiftsSerializer(dep)
        return Response(res.data, status=200)

def creat_or_udate_lunch(shift, lunchs):
    for lunch in lunchs:
        if "id" in lunch:
            print(lunch['id'])
            ln = Lunch.objects.get(id=int(lunch['id']))
            ln.start = lunch['start']
            ln.end = lunch['end']
            ln.save()
        else:
            ln = Lunch(start=shift.start, end=shift.end, parent_id=shift.pk)
            ln.save()




@permission_classes([IsAuthenticated])
class Reserv2_Search(APIView):
    def get(self, request, pk):
        art = Reserv_2.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = Reserv_2Serializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Corparation_Search(APIView):
    def get(self, request, pk):
        art = Corparation.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CorparationSerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Company_Search(APIView):
    def get(self, request, pk):
        art = Company.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CompanySerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Factory_Search(APIView):
    def get(self, request, pk):
        art = Factory.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = FactorySerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Department_Search(APIView):
    def get(self, request, pk):
        art = Department.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = DepartmentSerializer(art, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class Agreagat_Search(APIView):
    def get(self, request, pk):
        art = Agreagat.objects.filter(parent=pk)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = AgreagatSerializer(art, many=True)
        return Response(serializer.data)
