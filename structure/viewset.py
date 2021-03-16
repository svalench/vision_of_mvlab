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
            if self.serializer_class.Meta.model.__name__ in structure:
                ind_struct = structure.index(self.serializer_class.Meta.model.__name__)
                parent_name = structure[ind_struct - 1]
                id = self.find_parent_id(parent_name, request.data['parent'],structure)
                try:
                    id = self.find_parent_id(parent_name, request.data['parent'],structure)
                    request.data['parent'] = id
                except:
                    raise ValidationError(
                        'Create ' + str(BASE_STRUCTURE[ind]) + '. Not found ' + parent_name + ' with pk %s' % request.data[
                            'parent'])
        else:
            try:
                first_object = structure[0]
                if self.serializer_class.Meta.model.__name__ == first_object and self.serializer_class.Meta.model.__name__ != "Reserv_1":
                    request.data['parent'] = globals()[new_base[0]].objects.all().first().id
            except:
                raise ValidationError(
                    "See viewset in structure class MetaView error in create object if not find parent in query")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def find_parent_id(self, parentname, prentid,structure):
        ind = BASE_STRUCTURE.index(self.serializer_class.Meta.model.__name__)
        ind_parent = BASE_STRUCTURE.index(parentname)
        counter = ind - ind_parent
        a = globals()[parentname].objects.get(pk=prentid)
        print(a.child_model())
        try:
            c = list(a.child_model())[0]
        except:
            return prentid
        for i in range(counter):
            try:
                c = list(c.child_model())[0]
            except:
                continue
        print(c)
        return c.id

    def validate_parent(self, value):
        """
        Validate parent row
        """
        return value

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        ob = FirstObject.objects.all().first()
        structure = ob.listModels
        ind = BASE_STRUCTURE.index(self.serializer_class.Meta.model.__name__)
        new_base = list(BASE_STRUCTURE[:ind])
        new_base.reverse()
        if 'parent' in request.data or self.serializer_class.Meta.model.__name__ != "Reserv_1":

            for index, item in enumerate(structure):
                if self.serializer_class.Meta.model.__name__ == item:
                    if index == 0:
                        print(kwargs)
                        this = globals()[structure[index]].objects.get(pk=kwargs['pk'])
                        parent = this.parent
                        request.data['parent'] = parent.id
                    else:
                        parent = globals()[structure[index - 1]].objects.get(pk=request.data['parent'])
                    print(parent)
                    try:
                        c = list(parent.child_model())[0]
                        if c.__class__.__name__ not in structure:
                            request.data['parent'] = c.id
                            break
                    except:
                        pass


        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


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
