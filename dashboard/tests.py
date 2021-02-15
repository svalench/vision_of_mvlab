from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import UserP
from rest_framework.authtoken.models import Token
from dashboard.models import Role
from dashboard.models import Dashboard
import datetime
from dashboard.models import DurationIntervalDay
import random
from django.db import connection
from project_v_0_0_1.settings import dist_table
import json
from structure.models import *


# Create your tests here.
class Test_dashboard(APITestCase):
    def setUp(self):
        # создание имя дашборда
        name_dash = ["DurationIntervalDay", "Storehouse", "EditionDay", "SumexpenseDay", "EnergyConsumptionDay",
                     "SpecificConsumptionDay"]
        for dash in name_dash:
            Dash = Dashboard(name=dash)
            Dash.save()
        # создание супер пользователя
        self.superuser = UserP.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.token, created = Token.objects.get_or_create(user=self.superuser)
        self.token.save()
        # создание роли
        self.rol = Role(name="direk")
        self.rol.save()
        # подключение пользователя к роли и роли к дашборду
        self.rol.user.add(self.superuser)
        name_dash = Dashboard.objects.all()
        for Dash in name_dash:
            self.rol.dashboard.add(Dash)  # self.dashboard)
        # создание таблицы(не джанго)
        # with connection.cursor() as cursor:
        #     engine = connection.vendor
        #     if engine == 'sqlite':
        #         sql = '''CREATE TABLE ''' + dist_table['DurationIntervalDay'][
        #             0] + ''' (start time, end time, date date)'''
        #     elif engine == 'postgresql':
        #         sql = '''CREATE TABLE ''' + dist_table['DurationIntervalDay'][
        #             0] + ''' (start time, end time, date date)'''
        #     cursor.execute(sql)
        #     for i in range(10):
        #         cursor.execute("""INSERT INTO """ +  dist_table['DurationIntervalDay'][0] +
        #                        """ VALUES ('""" + str(datetime.time(random.randint(i, i+2), random.randint(i, i+20),random.randint(i, i+20))) +
        #                        """', '""" + str(datetime.time(random.randint(i+3, i+5), random.randint(i+6, i+9),random.randint(i+6, i+9))) +
        #                        """', '""" + str(datetime.date(2020, 11, 21)) + "' )")
        # # Заполнение базы DurationIntervalDay
        # start1 = datetime.time(12, 34, 45)
        # end1 = datetime.time(14, 54, 56)
        # start2 = datetime.time(17, 34, 45)
        # end2 = datetime.time(18, 54, 56)
        # for i in range(1, 31):
        #     if random.randint(1, 2) == 2:
        #         d = DurationIntervalDay(start=start1, end=end1, date=datetime.date(2020, 11, i))
        #         d.save()
        #         d = DurationIntervalDay(start=start2, end=end2, date=datetime.date(2020, 11, i))
        #         d.save()
        #     else:
        #         d = DurationIntervalDay(start=start1, end=end1, date=datetime.date(2020, 11, i))
        #         d.save()
        # добавление структуры
        data1 = {
            "levlel_0": 0,
            "levlel_1": 1,
            "levlel_2": 2,
            "levlel_3": 3,
            "levlel_4": 4,
            "levlel_5": 5,
            "levlel_6": 6,
            "levlel_7": 7
        }
        data2 = {
            "name": "asd",
            "customer": "asd",
            "contract": "asd",
            "structure": data1
        }
        json_str = json.dumps(data2)
        url = reverse("wizard_sep1")
        response = self.client.post(url, data=json_str, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["data"], "success")
        # проверка созданной структуры
        response = self.client.get('/settings/get_structure/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["name"], "asd")
        self.assertEqual(json_response["customer"], "asd")
        self.assertEqual(json_response["contract"], "asd")
        self.assertEqual(json_response["structure"]["levlel_0"], 0)
        self.assertEqual(json_response["structure"]["levlel_1"], 1)
        self.assertEqual(json_response["structure"]["levlel_2"], 2)
        self.assertEqual(json_response["structure"]["levlel_3"], 3)
        self.assertEqual(json_response["structure"]["levlel_4"], 4)
        self.assertEqual(json_response["structure"]["levlel_5"], 5)
        self.assertEqual(json_response["structure"]["levlel_6"], 6)
        self.assertEqual(json_response["structure"]["levlel_7"], 7)
        # добавление элементов в структуру
        data = {
            "name": "asdasd"
        }
        json_data = json.dumps(data)
        a = FirstObject.objects.all().first()
        response = self.client.post('/structure/Reserv_1/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        print(response.content)
        response = self.client.get("/structure/Reserv_1/", HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_durat(self):
        # проверка дней
        url = reverse("duration_day", kwargs={"date": "2020-11-21"})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        data = json.loads(response.content.decode('utf8'))
        asr = '%H:%M:%S'
        for i in data["interval"]:
            self.assertEqual(type(i["start"]), str)
            if type(i["start"]) is str:
                t = datetime.datetime.strptime(i["start"], asr).time()
                date = datetime.time(12, 12, 12)
                self.assertEqual(type(t), datetime.time)
            self.assertEqual(type(i["end"]), str)
            if type(i["end"]) is str:
                t = datetime.datetime.strptime(i["end"], asr).time()
                date = datetime.time(12, 12, 12)
                self.assertEqual(type(t), datetime.time)
            self.assertEqual(type(i["duration"]), float)
        self.assertEqual(type(data["sum"]), float)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверка смены
        url = reverse("duration_shift", kwargs={"date": "2020-11-21", "id": 2})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        data = json.loads(response.content.decode('utf8'))
        for i in data["interval"]:
            self.assertEqual(type(i["start"]), str)
            if type(i["start"]) is str:
                asr = '%H:%M:%S'
                t = datetime.datetime.strptime(i["start"], asr).time()
                date = datetime.time(12, 12, 12)
                self.assertEqual(type(t), datetime.time)
            self.assertEqual(type(i["end"]), str)
            if type(i["end"]) is str:
                asr = '%H:%M:%S'
                t = datetime.datetime.strptime(i["end"], asr).time()
                date = datetime.time(12, 12, 12)
                self.assertEqual(type(t), datetime.time)
            self.assertEqual(type(i["duration"]), float)
        self.assertEqual(type(data["sum"]), float)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
