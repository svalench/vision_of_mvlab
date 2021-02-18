import json
import socket

from django.db import connection
from rest_framework.exceptions import ValidationError

from dashboard.teldefax_dashboard import TransitionReadings, GenerationOfElectricity, Status
from rest_framework.views import APIView
from rest_framework.response import Response

from project_v_0_0_1.settings import SOCKET_PORT_SEREVER


def get_dashboard(data):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect(('128.65.54.166', 8084))
        print(data)
        data = json.dumps(data).encode('utf-8')
    except:
        return {"error":"no connection to socket"}
    try:
        sock.send(data)
    except:
        sock.close()
    try:
        res = sock.recv(1024)
    except:
        return {"error":"no connection to socket"}
    print(res)
    sock.close()
    return json.loads(res)

class teldafax(TransitionReadings, GenerationOfElectricity, Status, APIView):
    """
    Класс для вывода данных для dashboard
    """
    def get(self, request):
        name_dash = self.request.query_params.get('name')
        a = {
            "methane": self.methane(),
            "carbondioxide": self.carbondioxide(),
            "oxygen": self.oxygen(),
            "pressure_in": self.pressure_in(),
            "pressure_out": self.pressure_out(),
            "consumption": self.consumption(),
            "temperature": self.temperature()
        }
        return Response(a)

class TeldafaxErrorTablesAndStatusInIt(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            engine = connection.vendor
            if engine == 'sqlite':
                sql = '''SELECT count(*) FROM sqlite_master WHERE type="table" AND name="'''
            elif engine == 'postgresql':
                sql = """SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_name ='"""
            sql = sql + "mvlab_alarms" + ";'"
            cursor.execute(sql)
            a = cursor.fetchall()[0][0]
        if a:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM mvlab_alarms WHERE status=1;"""
                cursor.execute(sql)
                res_alarms = cursor.fetchall()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM mvlab_warnings WHERE status=1;"""
                cursor.execute(sql)
                res_warnings = cursor.fetchall()
                res = {"alarms":res_alarms, "warnings":res_warnings}
        else:
            res={"error":"no Table Error in DB"}
        return Response(res)

class Teldafax_status(APIView):
    def get(self, request):
        data = get_dashboard({"dash_teldafax":True})
        if "data1" in data:
            data1 = data['data1']
            data2 = data["data2"]
        else:
            raise ValidationError("Нет связи с микросервисом")
        try:
            res = {
                'power1': data1["power1"],
                'power2': data1["power2"],
                'power3': data1["power3"],
                'power4': data1["power4"],
                'sum_power': data1["sum_power"],
                'work_status': data2["work_status"],
                'pump_p301_status': data2["pump_p301_status"],
                'valve_B1101_status': data2["valve_B1101_status"],
                'valve_B1601_status': data2["valve_B1601_status"],
                'compres_V501_status':data2["compres_V501_status"],
                'compres_V502_status':data2["compres_V502_status"],
                'compres_V503_status':data2["compres_V503_status"],
                'generator_D601_status1':data2["generator_D601_status1"],
                'generator_D601_status2':data2["generator_D601_status2"],
                'generator_D602_status1':data2["generator_D602_status1"],
                'generator_D602_status2':data2["generator_D602_status2"],
                'generator_D603_status1':data2["generator_D603_status1"],
                'generator_D603_status2':data2["generator_D603_status2"],
                'generator_D604_status1':data2["generator_D604_status1"],
                'generator_D604_status2':data2["generator_D604_status2"],
                "fakel_A604":data2['fakel_A604']
            }
        except:
            raise ValidationError("Нет связи с плк")
        return Response(res)

class GetStatusConnectionsTeldafax(APIView):

    def get(self, request):
        data = get_dashboard({"sss": True})
        return Response(data)