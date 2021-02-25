from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from project_v_0_0_1.settings import BASE_STRUCTURE
from .models import *
from rest_framework.permissions import IsAuthenticated

from .serializer import *

from rest_framework.views import APIView
import json


class MetaView:
    """
    Класс для переопределения базовых методов ModelViewSet
    
     Methods
    =========
    
    - create - проверяем есть ли в созданной структуре родитель если нет то id передан от уровня выше и мы переопределям id
    """

    def create(self, request, *args, **kwargs):
        """ переопределенный метод для проверки приходящих данных. Если parent указан не для предыдущей связванной модели то переопределяем его"""
        ob = FirstObject.objects.all().first()
        structure = ob.listModels
        ind = BASE_STRUCTURE.index(self.serializer_class.Meta.model.__name__)
        new_base = list(BASE_STRUCTURE[:ind])
        new_base.reverse()
        if 'parent' in request.data:
            for b in new_base:
                if b in structure:
                    try:
                        a = globals()[b].objects.get(pk=request.data['parent'])
                        i = new_base.index(b)
                        str_query = new_base[:i]
                        str_query.reverse()
                        if(str_query):
                            for q in str_query:
                                if q == "Reserv_1":
                                    c = Reserv_1.all().first()
                                    break
                                if str_query.index(q) == 0:
                                    c = a.child_model().first()
                                    continue
                                c = a.child_model().first()
                            request.data['parent'] = c.id
                    except:
                        raise ValidationError('Create '+str(BASE_STRUCTURE[ind])+' . Not found '+b+' with pk %s' % request.data['parent'])
                break
        else:
            try:
                first_object = structure[0]
                if self.serializer_class.Meta.model.__name__ == first_object:
                    request.data['parent'] = globals()[new_base[1]].objects.all().first().id
                    print('========================================================')
                    print('========================IS GREAT!!!!!!!========================')
            except:
                raise ValidationError("See viewset in structure class MetaView error in create object if not find parent in query")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class Reserv_1View(MetaView, viewsets.ModelViewSet):
    serializer_class = Reserv_1Serializer
    queryset = Reserv_1.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(True)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(Reserv_1View, self).get_permissions()


# class Reserv_1View(APIView):
#     def post(self, request):
#         data = request.body.decode('utf8')
#         data_json = json.loads(data)
#         a = FirstObject.objects.all().first()
#         print(a.start_object)
#         a = Reserv_1(name=data_json["name"])
#         a.save()
#         return Response({"succes"})


class Reserv_2View(MetaView, viewsets.ModelViewSet):
    queryset = Reserv_2.objects.all()
    serializer_class = Reserv_2Serializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(Reserv_2View, self).get_permissions()


class CorparationView(MetaView, viewsets.ModelViewSet):
    queryset = Corparation.objects.all()
    serializer_class = CorparationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(CorparationView, self).get_permissions()


class CompanyView(MetaView, viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(CompanyView, self).get_permissions()


class FactoryView(MetaView, viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(FactoryView, self).get_permissions()


class DepartmentView(MetaView, viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentShiftsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(DepartmentView, self).get_permissions()


class ShiftView(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(ShiftView, self).get_permissions()


class LunchView(viewsets.ModelViewSet):
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(LunchView, self).get_permissions()


class AgreagatView(MetaView, viewsets.ModelViewSet):
    queryset = Agreagat.objects.all()
    serializer_class = AgreagatSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(AgreagatView, self).get_permissions()


class SensorsView(MetaView, viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(SensorsView, self).get_permissions()
