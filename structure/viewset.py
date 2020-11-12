from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import *
from rest_framework.permissions import IsAuthenticated

from .serializer import *

class Reserv_1View(viewsets.ModelViewSet):
    queryset = Reserv_1.objects.all()
    serializer_class = Reserv_1Serializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(Reserv_1View, self).get_permissions()


class Reserv_2View(viewsets.ModelViewSet):
    queryset = Reserv_2.objects.all()
    serializer_class = Reserv_2Serializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(Reserv_2View, self).get_permissions()



class CorparationView(viewsets.ModelViewSet):
    queryset = Corparation.objects.all()
    serializer_class = CorparationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(CorparationView, self).get_permissions()

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(CompanyView, self).get_permissions()



class FactoryView(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(FactoryView, self).get_permissions()


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

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



class AgreagatView(viewsets.ModelViewSet):
    queryset = Agreagat.objects.all()
    serializer_class = AgreagatSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(AgreagatView, self).get_permissions()

    def create(self, request, *args, **kwargs):
        ob = FirstObject.objects.all().first()
        structure = ob.listModels
        print(request.data)
        if 'Department' in structure:
            pass
        else:
            if 'Factory' in structure:
                try:
                    a = Factory.objects.get(pk=request.data['parent'])
                    request.data['parent'] = a.department_set.all().first().id
                except:
                    raise ValidationError('Not found Factory with pk %s'%request.data['parent'])
            else:
                if 'Company' in structure:
                    try:
                        a = Company.objects.get(pk=request.data['parent'])
                        request.data['parent'] = a.factory_set.all().first().department_set.all().first().id
                    except:
                        raise ValidationError('Not found Company with pk %s' % request.data['parent'])
                    else:
                        if 'Corparation' in structure:
                            try:
                                a = Corparation.objects.get(pk=request.data['parent'])
                                request.data['parent'] = a.company_set.all().first().factory_set.all().first().department_set.all().first().id
                            except:
                                raise ValidationError('Not found Corparation with pk %s' % request.data['parent'])
                        else:
                            if 'Reserv_2' in structure:
                                try:
                                    a = Reserv_2.objects.get(pk=request.data['parent'])
                                    request.data[
                                        'parent'] = a.corparation_set.all().first().company_set.all().first().factory_set.all().first().department_set.all().first().id
                                except:
                                    raise ValidationError('Not found Reserv_2 with pk %s' % request.data['parent'])
                            else:
                                if 'Reserv_1' in structure:
                                    try:
                                        a = Reserv_1.objects.get(pk=request.data['parent'])
                                        request.data[
                                            'parent'] = a.reserv_2_set.all().first().corparation_set.all().first().company_set.all().first().factory_set.all().first().department_set.all().first().id
                                    except:
                                        raise ValidationError('Not found Reserv_1 with pk %s' % request.data['parent'])
                                else:
                                    request.data['parent'] = Reserv_1.objects.all().firest()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class SensorsView(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(SensorsView, self).get_permissions()