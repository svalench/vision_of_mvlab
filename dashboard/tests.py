from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import UserP
from rest_framework.authtoken.models import Token
from dashboard.models import Role, SpecificConsumptionDay
from dashboard.models import Dashboard, Storehouse, Substance, DateValue, EditionDay
import datetime
from dashboard.models import DurationIntervalDay, SumexpenseDay, EnergyConsumptionDay
import random
from django.db import connection
from project_v_0_0_1.settings import dist_table
import json


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
        self.client.post(url, data=json_str, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type="application/json")
        # добавление элементов в структуру
        data = {
            "name": "asdasd"
        }
        json_data = json.dumps(data)
        self.client.post('/structure/Reserv_1/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "name": "asd",
            "parent": 1
        }
        json_data = json.dumps(data)
        self.client.post("/structure/Reserv_2/", data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "name": "asd",
            "parent": 1
        }
        json_data = json.dumps(data)
        self.client.post('/structure/Corparation/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "name": "asd",
            "parent": 1
        }
        json_data = json.dumps(data)
        self.client.post("/structure/Company/", data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "parent": 1,
            "name": "asd",
            "address": "asd"
        }
        json_data = json.dumps(data)
        self.client.post('/structure/Factory/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data_lanch1 = {
            "start": "03:15:00",
            "end": "04:15:00"
        }
        data_lanch2 = {
            "start": "07:15:00",
            "end": "08:15:00"
        }
        data_lanch3 = {
            "start": "13:15:00",
            "end": "14:15:00"
        }
        data_lanch4 = {
            "start": "19:15:00",
            "end": "20:15:00"
        }
        data_shifts1 = {
            "start": "00:00:00",
            "end": "06:00:00",
            "lanch": [data_lanch1]
        }
        data_shifts2 = {
            "start": "06:00:00",
            "end": "12:00:00",
            "lanch": [data_lanch2]
        }
        data_shifts3 = {
            "start": "12:00:00",
            "end": "18:00:00",
            "lanch": [data_lanch3]
        }
        data_shifts4 = {
            "start": "18:00:00",
            "end": "23:55:00",
            "lanch": [data_lanch4]
        }

        data = {
            "name": "asd",
            "parent": 1,
            "shifts": [data_shifts1, data_shifts2, data_shifts3, data_shifts4]
        }
        json_data = json.dumps(data)
        self.client.post('/settings/create/department/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "name": "asd",
            "parent": 1
        }
        json_data = json.dumps(data)
        self.client.post('/structure/Agreagat/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        data = {
            "name": "asd",
            "parent": 1,
            "designation": "asd"
        }
        json_data = json.dumps(data)
        self.client.post('/structure/Sensors/', data=json_data, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        return 0

    def test_get_struct(self):
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

    def test_get_reserv1(self):
        response = self.client.get("/structure/Reserv_1/", HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asdasd")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reserv2(self):
        url = reverse("searchReserv2", kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_corparation(self):
        url = reverse('searchCorparation', kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)

    def test_get_company(self):
        url = reverse('searchCompany', kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)

    def test_get_factory(self):
        url = reverse('searchFactory', kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["address"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)

    def test_get_search_department(self):
        url = reverse('searchDepartment', kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)

    def test_get_agreagat(self):
        url = reverse('searchAgreagat', kwargs={"pk": 1})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token), content_type='application/json')
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["id"], 1)
        self.assertEqual(json_response[0]["name"], "asd")
        self.assertEqual(json_response[0]["parent"], 1)

    def test_durat(self):

        # создание таблицы(не джанго)

        with connection.cursor() as cursor:
            engine = connection.vendor
            if engine == 'sqlite':
                sql = '''CREATE TABLE ''' + dist_table['DurationIntervalDay'][
                    0] + ''' (value real, now_time datetime)'''
            elif engine == 'postgresql':
                sql = '''CREATE TABLE ''' + dist_table['DurationIntervalDay'][
                    0] + ''' (value real, now_time datetime)'''
            cursor.execute(sql)
            for i in range(1):
                cursor.execute("""INSERT INTO """ + dist_table['DurationIntervalDay'][0] +
                               """ VALUES ('""" + str(1) +
                               """', '""" + str(datetime.datetime(2020, 11, 21, 10, 21, 36)) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['DurationIntervalDay'][0] +
                               """ VALUES ('""" + str(0) +
                               """', '""" + str(datetime.datetime(2020, 11, 21, 11, 3, 12)) + "' )")

        # Заполнение базы DurationIntervalDay

        start1 = datetime.time(hour=12, minute=34, second=45)
        end1 = datetime.time(hour=14, minute=54, second=56)
        start2 = datetime.time(17, 34, 45)
        end2 = datetime.time(18, 54, 56)
        for i in range(1, 31):
            if random.randint(1, 2) == 2:
                d = DurationIntervalDay(start=start1, end=end1, date=datetime.date(2020, 11, i))
                d.save()
                d = DurationIntervalDay(start=start2, end=end2, date=datetime.date(2020, 11, i))
                d.save()
            else:
                d = DurationIntervalDay(start=start1, end=end1, date=datetime.date(2020, 11, i))
                d.save()

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

    def test_remainder(self):
        # заполнение базы
        a = Storehouse(name="number 1")
        a.save()
        b = Storehouse(name="number 2")
        b.save()
        k = ["PEN", "POL", "ISO"]
        for i in k:
            sub = Substance(name=i, short_name=i, table_name=i, parent=a)
            sub.save()
            sub1 = Substance(name=i+"1", short_name=i, table_name=i+"1", parent=a)
            sub1.save()
            dat = datetime.date(2020, 11, 21)
            val = random.randint(0, 10000) / 100
            c = DateValue(date=dat, value=val, parent=sub)
            c.save()
            c = DateValue(date=dat, value=val, parent=sub1)
            c.save()
        for i in k:
            sub = Substance(name=i, short_name=i, table_name=i, parent=b)
            sub.save()
            dat = datetime.date(2020, 11, 21)
            val = random.randint(0, 10000)/100
            c = DateValue(date=dat, value=val, parent=sub)
            c.save()

        # запрос данных остатков
        date = datetime.date(2020,11,21)
        url = reverse('remainder', kwargs={"date": '2020-11-21'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["storehouse"][0]["name"], "number 1")
        self.assertEqual(json_response["storehouse"][1]["name"], "number 2")
        self.assertEqual(type(json_response["storehouse"][0]["iso"]), list)
        for i in json_response["storehouse"][0]["iso"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["storehouse"][0]["pol"]), list)
        for i in json_response["storehouse"][0]["pol"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["storehouse"][0]["pen"]), list)
        for i in json_response["storehouse"][0]["pen"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["storehouse"][1]["iso"]), list)
        for i in json_response["storehouse"][1]["iso"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["storehouse"][1]["pol"]), list)
        for i in json_response["storehouse"][1]["pol"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["storehouse"][1]["pen"]), list)
        for i in json_response["storehouse"][1]["pen"]:
            self.assertEqual(type(i), float)
        self.assertEqual(type(json_response["in_total"]), dict)
        self.assertEqual(type(json_response["in_total"]["iso"]), float)
        self.assertEqual(type(json_response["in_total"]["pol"]), float)
        self.assertEqual(type(json_response["in_total"]["pen"]), float)

    def test_edition(self):

        #заполнение базы

            #таблица джанго
        date =datetime.date(2020, 10, 1)
        delta = datetime.timedelta(days=1)
        for i in range(1, 70):
            a = EditionDay(date=date, suitable=12.1, substandard=32.1, defect=214.4, flooded=43.7, sum=324.5)
            a.save()
            date = date + delta

            #таблица не джанго
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE ''' + dist_table['EditionDay'] + ''' (value real, now_time datetime, status INTEGER)'''
            cursor.execute(sql)
            date = datetime.datetime(2020, 11, 15, 4, 5, 5)
            time_delta_hor = datetime.timedelta(hours=6)
            k = [0, 1, 2, 3]
            for i in range(40):
                for j in k:
                    cursor.execute("""INSERT INTO """ + dist_table['EditionDay'] +
                                   """ VALUES ('""" + str(random.randint(1, 10000)/100) +
                                   """', '""" + str(date) +
                                   """', '""" + str(j) + "' )")
                date = date + time_delta_hor

        #запрос для месяца
        url = reverse('edition_month', kwargs={"date": "2020-11-22"})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable']), float)
        self.assertEqual(type(json_response['change_suitable']), float)
        self.assertEqual(type(json_response['substandard']), float)
        self.assertEqual(type(json_response['change_substandard']), float)
        self.assertEqual(type(json_response['defect']), float)
        self.assertEqual(type(json_response['change_defect']), float)
        self.assertEqual(type(json_response['flooded']), float)
        self.assertEqual(type(json_response['change_flooded']), float)
        self.assertEqual(type(json_response['sum']), float)
        self.assertEqual(type(json_response['change_sum']), float)

        #запрос для дня
        url = reverse('edition_day', kwargs={"date": "2020-11-21"})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable']), float)
        self.assertEqual(type(json_response['change_suitable']), float)
        self.assertEqual(type(json_response['substandard']), float)
        self.assertEqual(type(json_response['change_substandard']), float)
        self.assertEqual(type(json_response['defect']), float)
        self.assertEqual(type(json_response['change_defect']), float)
        self.assertEqual(type(json_response['flooded']), float)
        self.assertEqual(type(json_response['change_flooded']), float)
        self.assertEqual(type(json_response['sum']), float)
        self.assertEqual(type(json_response['change_sum']), float)

        #запрос смены
        url = reverse('edition_shift', kwargs={"date": "2020-11-20", "id": 3})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable']), float)
        self.assertEqual(type(json_response['change_suitable']), float)
        self.assertEqual(type(json_response['substandard']), float)
        self.assertEqual(type(json_response['change_substandard']), float)
        self.assertEqual(type(json_response['defect']), float)
        self.assertEqual(type(json_response['change_defect']), float)
        self.assertEqual(type(json_response['flooded']), float)
        self.assertEqual(type(json_response['change_flooded']), float)
        self.assertEqual(type(json_response['sum']), float)
        self.assertEqual(type(json_response['change_sum']), float)

    def test_sumexpen(self):

        #заполнение базы

            # таблицы джанго
        date = datetime.date(2020, 11, 1)
        time_del = datetime.timedelta(days=1)
        for i in range(32):
            a = SumexpenseDay(iso=random.randint(0,100)/10, pol=random.randint(0,100)/10, pen=random.randint(0,100)/10,
                              kat1=random.randint(0,100)/10, kat2=random.randint(0,100)/10,
                              kat3=random.randint(0,100)/10, date=date)
            a.save()
            date = date + time_del

            # таблицы вне джанго
        with connection.cursor() as cursor:
            for i in dist_table['SumexpenseDay']['iso']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SumexpenseDay']['pol']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SumexpenseDay']['pen']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SumexpenseDay']['kat1']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SumexpenseDay']['kat2']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SumexpenseDay']['kat3']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            date = datetime.datetime(2020, 11, 15, 4, 5, 5)
            time_delta_hor = datetime.timedelta(hours=6)
            for i in range(40):
                for j in dist_table['SumexpenseDay']['iso']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000)/100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SumexpenseDay']['pol']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SumexpenseDay']['pen']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SumexpenseDay']['kat1']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SumexpenseDay']['kat2']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SumexpenseDay']['kat3']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                date = date + time_delta_hor

        # проверка для месяца
        url = reverse('sumexpense_month', kwargs={'date': '2020-11-21'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['iso']), float)
        self.assertEqual(type(json_response['pol']), float)
        self.assertEqual(type(json_response['pen']), float)
        self.assertEqual(type(json_response['kat1']), float)
        self.assertEqual(type(json_response['kat2']), float)
        self.assertEqual(type(json_response['kat3']), float)

        # проверка для дня
        url = reverse('sumexpense_day', kwargs={'date': '2020-11-21'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['iso']), float)
        self.assertEqual(type(json_response['pol']), float)
        self.assertEqual(type(json_response['pen']), float)
        self.assertEqual(type(json_response['kat1']), float)
        self.assertEqual(type(json_response['kat2']), float)
        self.assertEqual(type(json_response['kat3']), float)

        # проверка для смены
        url = reverse('sumexpense_shift', kwargs={'date': '2020-11-21', 'id': 3})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['iso']), float)
        self.assertEqual(type(json_response['pol']), float)
        self.assertEqual(type(json_response['pen']), float)
        self.assertEqual(type(json_response['kat1']), float)
        self.assertEqual(type(json_response['kat2']), float)
        self.assertEqual(type(json_response['kat3']), float)

    def test_energy(self):

        # заполнение базы

            # таблица джанго
        date = datetime.date(2020, 11, 1)
        delta_day = datetime.timedelta(days=1)
        for i in range(70):
            a = EnergyConsumptionDay(input1=random.randint(1,1000)/10, input2=random.randint(1,1000)/10, gas=random.randint(1,1000)/10, date=date)
            a.save()
            date = date + delta_day

            # таблицы не джанго
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE ''' + dist_table['EnergyConsumptionDay']['input1'] + ''' (value real, now_time datetime)'''
            cursor.execute(sql)
            sql = '''CREATE TABLE ''' + dist_table['EnergyConsumptionDay']['input2'] + ''' (value real, now_time datetime)'''
            cursor.execute(sql)
            sql = '''CREATE TABLE ''' + dist_table['EnergyConsumptionDay']['gas'] + ''' (value real, now_time datetime)'''
            cursor.execute(sql)
            date = datetime.datetime(2020, 11, 1, 0, 15, 0)
            delta_time = datetime.timedelta(hours=6)
            for i in range(124):
                cursor.execute("""INSERT INTO """ + dist_table['EnergyConsumptionDay']['input1'] +
                               """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['EnergyConsumptionDay']['input2'] +
                               """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['EnergyConsumptionDay']['gas'] +
                               """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                               """', '""" + str(date) + "' )")
                date = date + delta_time

        # проверка месяц
        url = reverse('energyconsumption_month', kwargs={'date': '2020-11-29'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['input1']), float)
        self.assertEqual(type(json_response['input2']), float)
        self.assertEqual(type(json_response['gas']), float)

        # проверка дня
        url = reverse('energyconsumption_day', kwargs={'date': '2020-11-20'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['input1']), float)
        self.assertEqual(type(json_response['input2']), float)
        self.assertEqual(type(json_response['gas']), float)

        # проверка для смены
        url = reverse('energyconsumption_shift', kwargs={'date': '2020-11-21', 'id': 3})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['input1']), float)
        self.assertEqual(type(json_response['input2']), float)
        self.assertEqual(type(json_response['gas']), float)

    def test_specif(self):

        # добавление в базу

            # таблица джанго
        date = datetime.date(2020, 11, 1)
        delta_day = datetime.timedelta(days=1)
        for i in range(32):
            a = SpecificConsumptionDay(iso=random.randint(1,1000)/10,
                                       pol=random.randint(1,1000)/10,
                                       pen=random.randint(1,1000)/10,
                                       kat1=random.randint(1,1000)/10,
                                       kat2=random.randint(1,1000)/10,
                                       kat3=random.randint(1,1000)/10,
                                       date=date)
            a.save()
            date = date +delta_day

            # таблицы не джанго
        with connection.cursor() as cursor:
            for i in dist_table['SpecificConsumptionDay']['iso']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SpecificConsumptionDay']['pol']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SpecificConsumptionDay']['pen']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SpecificConsumptionDay']['kat1']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SpecificConsumptionDay']['kat2']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            for i in dist_table['SpecificConsumptionDay']['kat3']:
                cursor.execute('''CREATE TABLE ''' + i + ''' (value real, now_time datetime)''')
            date = datetime.datetime(2020, 11, 1, 0, 15, 0)
            delta_time = datetime.timedelta(hours=6)
            for i in range(124):
                for j in dist_table['SpecificConsumptionDay']['iso']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SpecificConsumptionDay']['pol']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SpecificConsumptionDay']['pen']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SpecificConsumptionDay']['kat1']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SpecificConsumptionDay']['kat2']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                for j in dist_table['SpecificConsumptionDay']['kat3']:
                    cursor.execute("""INSERT INTO """ + j + """ VALUES ('""" + str(random.randint(1, 10000) / 100) +
                                   """', '""" + str(date) + "' )")
                date = date + delta_time

            # проверка месяца
            url = reverse('specificconsumption_month', kwargs={'date': '2020-11-30'})
            response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
            json_response = json.loads(response.content.decode('utf8'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(type(json_response['iso']), float)
            self.assertEqual(type(json_response['pol']), float)
            self.assertEqual(type(json_response['pen']), float)
            self.assertEqual(type(json_response['kat1']), float)
            self.assertEqual(type(json_response['kat2']), float)
            self.assertEqual(type(json_response['kat3']), float)

            # проверка дня
            url = reverse('specificconsumption_day', kwargs={'date': '2020-11-30'})
            response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
            json_response = json.loads(response.content.decode('utf8'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(type(json_response['iso']), float)
            self.assertEqual(type(json_response['pol']), float)
            self.assertEqual(type(json_response['pen']), float)
            self.assertEqual(type(json_response['kat1']), float)
            self.assertEqual(type(json_response['kat2']), float)
            self.assertEqual(type(json_response['kat3']), float)

            # проверка смены
            url = reverse('specificconsumption_shift', kwargs={'date': '2020-11-30', 'id': 3})
            response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
            json_response = json.loads(response.content.decode('utf8'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(type(json_response['iso']), float)
            self.assertEqual(type(json_response['pol']), float)
            self.assertEqual(type(json_response['pen']), float)
            self.assertEqual(type(json_response['kat1']), float)
            self.assertEqual(type(json_response['kat2']), float)
            self.assertEqual(type(json_response['kat3']), float)

    def test_compar(self):

        # заполнение базы

            # таблица джанго
        date = datetime.date(2020, 11, 1)
        delta_day = datetime.timedelta(days=1)
        for i in range(80):
            a = EditionDay(suitable=random.randint(1, 1000)/100,
                           substandard=random.randint(1, 1000)/100,
                           defect=random.randint(1, 1000)/100,
                           flooded=random.randint(1, 1000)/100,
                           sum=random.randint(1, 1000)/100,
                           date=date)
            a.save()
            date = date + delta_day

            # таблица не джанго
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE ''' + dist_table['EditionDay'] + ''' (value real, status INTEGER, now_time datetime)'''
            cursor.execute(sql)
            date = datetime.datetime(2020, 11, 1, 0, 15, 0)
            delta_time = datetime.timedelta(hours=6)
            for i in range(124):
                for j in ['0', '1', '2', '3']:
                    cursor.execute("""INSERT INTO """ + dist_table['EditionDay'] +
                                   """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                                   """', '""" + j +
                                   """', '""" + str(date) + "' )")
                date = date + delta_time

        # проверка месяц
        url = reverse('comparison_month', kwargs={'date1': '2020-12-29', 'date2': '2020-11-29'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable1']), float)
        self.assertEqual(type(json_response['sui1_ch']), float)
        self.assertEqual(type(json_response['suitable2']), float)
        self.assertEqual(type(json_response['substandard1']), float)
        self.assertEqual(type(json_response['sub1_ch']), float)
        self.assertEqual(type(json_response['substandard2']), float)
        self.assertEqual(type(json_response['defect1']), float)
        self.assertEqual(type(json_response['def1_ch']), float)
        self.assertEqual(type(json_response['defect2']), float)
        self.assertEqual(type(json_response['flooded1']), float)
        self.assertEqual(type(json_response['flo_ch']), float)
        self.assertEqual(type(json_response['flooded2']), float)
        self.assertEqual(type(json_response['sum1']), float)
        self.assertEqual(type(json_response['sum1_ch']), float)
        self.assertEqual(type(json_response['sum2']), float)

        # проверка дня
        url = reverse('comparison_day', kwargs={'date1': '2020-12-29', 'date2': '2020-11-29'})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable1']), float)
        self.assertEqual(type(json_response['sui1_ch']), float)
        self.assertEqual(type(json_response['suitable2']), float)
        self.assertEqual(type(json_response['substandard1']), float)
        self.assertEqual(type(json_response['sub1_ch']), float)
        self.assertEqual(type(json_response['substandard2']), float)
        self.assertEqual(type(json_response['defect1']), float)
        self.assertEqual(type(json_response['def1_ch']), float)
        self.assertEqual(type(json_response['defect2']), float)
        self.assertEqual(type(json_response['flooded1']), float)
        self.assertEqual(type(json_response['flo_ch']), float)
        self.assertEqual(type(json_response['flooded2']), float)
        self.assertEqual(type(json_response['sum1']), float)
        self.assertEqual(type(json_response['sum1_ch']), float)
        self.assertEqual(type(json_response['sum2']), float)

        # проверка смены
        url = reverse('comparison_shift', kwargs={'date1': '2020-11-29', 'date2': '2020-11-28', 'id1': 2, 'id2': 2})
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        json_response = json.loads(response.content.decode('utf8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response['suitable1']), float)
        self.assertEqual(type(json_response['sui1_ch']), float)
        self.assertEqual(type(json_response['suitable2']), float)
        self.assertEqual(type(json_response['substandard1']), float)
        self.assertEqual(type(json_response['sub1_ch']), float)
        self.assertEqual(type(json_response['substandard2']), float)
        self.assertEqual(type(json_response['defect1']), float)
        self.assertEqual(type(json_response['def1_ch']), float)
        self.assertEqual(type(json_response['defect2']), float)
        self.assertEqual(type(json_response['flooded1']), float)
        self.assertEqual(type(json_response['flo_ch']), float)
        self.assertEqual(type(json_response['flooded2']), float)
        self.assertEqual(type(json_response['sum1']), float)
        self.assertEqual(type(json_response['sum1_ch']), float)
        self.assertEqual(type(json_response['sum2']), float)

    def test_teldafax(self):

        # заполнение базы
        with connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['methane'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['сarbon dioxide'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['oxygen'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['pressure in'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['pressure out'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['consumption'] +
                           ''' (value real, now_time datetime)''')
            cursor.execute('''CREATE TABLE ''' + dist_table['Taldefax']['TransitionReadings']['temperature'] +
                           ''' (value real, now_time datetime)''')
            date = datetime.datetime(2020, 11, 1, 0, 15, 0)
            delta_time = datetime.timedelta(hours=6)
            for i in range(124):
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['methane'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['сarbon dioxide'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['oxygen'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['pressure in'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['pressure out'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['consumption'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                cursor.execute("""INSERT INTO """ + dist_table['Taldefax']['TransitionReadings']['temperature'] +
                               """ VALUES ('""" + str(random.randint(1, 1000) / 10) +
                               """', '""" + str(date) + "' )")
                date = date + delta_time

            #проверка value
            url = reverse('teldafax_value')
            response = self.client.get(url)
            json_response = json.loads(response.content.decode('utf8'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(type(json_response['methane']), float)
            self.assertEqual(type(json_response['carbondioxide']), float)
            self.assertEqual(type(json_response['oxygen']), float)
            self.assertEqual(type(json_response['pressure_in']), float)
            self.assertEqual(type(json_response['pressure_out']), float)
            self.assertEqual(type(json_response['consumption']), float)
            self.assertEqual(type(json_response['temperature']), float)

            # проверка статуса
            url = reverse('teldafax_status')
            response = self.client.get(url)
            json_response = json.loads(response.content.decode('utf8'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(type(json_response['power1']), float)
            self.assertEqual(type(json_response['power2']), float)
            self.assertEqual(type(json_response['power3']), float)
            self.assertEqual(type(json_response['power4']), float)
            self.assertEqual(type(json_response['sum_power']), float)
            self.assertEqual(type(json_response['work_status']), int)
            self.assertEqual(type(json_response['pump_p301_status']), int)
            self.assertEqual(type(json_response['valve_B1101_status']), int)
            self.assertEqual(type(json_response['valve_B1601_status']), int)
            self.assertEqual(type(json_response['compres_V501_status']), int)
            self.assertEqual(type(json_response['compres_V502_status']), int)
            self.assertEqual(type(json_response['compres_V503_status']), int)
            self.assertEqual(type(json_response['generator_D601_status1']), int)
            self.assertEqual(type(json_response['generator_D601_status2']), int)
            self.assertEqual(type(json_response['generator_D602_status1']), int)
            self.assertEqual(type(json_response['generator_D602_status2']), int)
            self.assertEqual(type(json_response['generator_D603_status1']), int)
            self.assertEqual(type(json_response['generator_D603_status2']), int)
            self.assertEqual(type(json_response['generator_D604_status1']), int)
            self.assertEqual(type(json_response['generator_D604_status2']), int)
            self.assertEqual(type(json_response['fakel_A604']), int)
