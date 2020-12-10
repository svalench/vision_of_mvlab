from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from recorder.viewset import ValueSensorView
from structure.views import Parametrs
from structure.viewset import AgreagatView
from users.models import UserP
from rest_framework.authtoken.models import Token

factory = APIRequestFactory()

class RecorderTest(APITestCase):
    def setUp(self) -> None:
        self.superuser, self.token = createSuperuser()
        self.val_sens = {
        "name": "новый датчик 2",
        "name_connection": "сщттусе 1",
        "table_name": "mvlab_real_1",
        "up_level_alarm": 12.0,
        "down_level_alarm": 43.4,
        "up_level": 23.2,
        "down_level": 1.23,
        "rate_change": 0.23,
        "sensor": 1
    }
        self.data = self.data = {
            "name": "nikolosKefje",
            "customer": "ubisoft",
            "contract": "contr1.6",
            "structure": {
                "levlel_0": 6,
                "levlel_1": 7
            }
        }

    def test_save_structure(self):
        response = self.__create_struct()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def __create_val_sensor(self):
        request = factory.post('/recorder/structure/ValueSensor/', data=self.val_sens, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        response = ValueSensorView.as_view({'post':'create'})
        return response

    def __create_struct(self):
        request = factory.post('settings/wizard/step1', data=self.data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        response = Parametrs.step1(request)
        return response

    def __create_line(self):
        data = {'name': 'test_line_name', "parent": 1}
        request = factory.post('/settings/Factory', data=data, format='json',
                               HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = AgreagatView.as_view({'post': 'create'})
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
