from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your tests here.
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from structure.models import FirstObject, Department
from structure.views import Parametrs
from structure.viewset import CompanyView, FactoryView
from users.models import UserP

factory = APIRequestFactory()


class CreateStructTest(APITestCase):
    """
    Тестируем создание структуры предприятия

     Methods

     test_save_structure - тест на сохранение структуры
     test_create_3 - тес на создание компании
     test_create_4 - тест на создание завода
     test_create_5 - тест на создания агрегата
     test_create_dep_autamticly - тест на автоматическое создание департамента (при отсутсвии в структуре)
     __create_struct - метод для сохранения структуры
     __create_factory - метод сохраненич завода
     __create_company -  метод сохранеия компании


    """
    def setUp(self) -> None:
        self.superuser, self.token = createSuperuser()
        self.data = {
            "name": "nikolosKefje",
            "customer": "ubisoft",
            "contract": "contr1.6",
            "structure": {
                "levlel_0": 3,
                "levlel_1": 4,
                "levlel_2": 6,
                "levlel_3": 7
            }
        }

    def test_save_structure(self):
        response = self.__create_struct()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_3(self):
        self.__create_struct()
        response = self.__create_company()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_4(self):
        self.__create_struct()
        self.__create_company()
        response = self.__create_factory()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_dep_autamticly(self):
        self.__create_struct()
        self.__create_company()
        response = self.__create_factory()
        dep = Department.objects.get(pk=response.data['id'])
        self.assertEqual(dep.name, 'Базавая структуру')

    def test_create_5(self):
        self.__create_struct()
        factor = self.__create_factory()
        data = {
            "name": "Ceh otkachki mochi",
            "factory_id": factor.data['id'],
            "shifts": [
                {
                    "start": "00:00:00",
                    "end": "07:40:00",
                    "lanch": [
                        {
                            "start": "03:00:00",
                            "end": "03:15:00"
                        },
                        {
                            "start": "06:00:00",
                            "end": "06:20:00"
                        }

                    ]
                },
                {
                    "start": "07:40:00",
                    "end": "15:40:00",
                    "lanch": [
                        {
                            "start": "11:00:00",
                            "end": "11:30:00"
                        }
                    ]
                },
                {
                    "start": "15:40:00",
                    "end": "00:00:00",
                    "lanch": [
                        {
                            "start": "17:00:00",
                            "end": "17:15:00"
                        },
                        {
                            "start": "21:00:00",
                            "end": "21:30:00"
                        }

                    ]
                }
            ]
        }
        request = factory.post('/settings/create/department', data=data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        response = Parametrs.create_shift(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def __create_struct(self):
        request = factory.post('settings/wizard/step1', data=self.data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        response = Parametrs.step1(request)
        return response

    def __create_factory(self):
        com = self.__create_company()
        data = {'name': 'test_factory_name', "parent": com.data['id']}
        request = factory.post('/settings/Factory', data=data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = FactoryView.as_view({'post': 'create'})
        response = view(request)
        return response

    def __create_company(self):
        data = {'name': 'testname', "parent": 1}
        request = factory.post('/settings/Company', data=data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = CompanyView.as_view({'post': 'create'})
        response = view(request)
        return response


def createSuperuser():
    """
    авторизация суперпользовтеля для тестов
    """
    superuser = UserP.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
    token, created = Token.objects.get_or_create(user=superuser)
    token.save()
    return [superuser, token]
