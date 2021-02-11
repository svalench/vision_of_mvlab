from rest_framework.exceptions import ValidationError

from dashboard.teldefax_dashboard import TransitionReadings, GenerationOfElectricity, Status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.get_value_from_siemens_teldafax import PlcRemoteUse
from project_v_0_0_1.settings import PLC_init

class teldafax(TransitionReadings, GenerationOfElectricity, Status, APIView):
    """
    Класс для вывода данных для dashboard
    """
    def get(self, request):
        # name_dash = self.request.query_params.get('name')
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



class Teldafax_status(APIView):
    def get(self, request):
        # data = PlcRemoteUse(PLC_init["address"], PLC_init["rack"], PLC_init["slot"], PLC_init["port"])
        # data1 = data.get_dashboard_teldafax_value_power()
        # data2 = data.get_status_machine()
        #try:
        R = {
            'power1': 234,
            'power2': 321,
            'power3': 432,
            'power4': 234,
            'sum_power': 123,
            'work_status': 2,
            'pump_p301_status': 1,
            'valve_B1101_status': 0,
            'valve_B1601_status': 1,
            'compres_V501_status': 0,
            'compres_V502_status': 1,
            'compres_V503_status': 2,
            'generator_D601_status1': 0,
            'generator_D601_status2': 16,
            'generator_D602_status1': 1,
            'generator_D602_status2': 8,
            'generator_D603_status1': 2,
            'generator_D603_status2': 16,
            'generator_D604_status1': 4,
            'generator_D604_status2': 0,
            'fakel_A604': 1
        }
        #except:
        #    raise ValidationError("Нет связи с плк")
        return Response(R)

# {
#                 'power1': data1["power1"],
#                 'power2': data1["power2"],
#                 'power3': data1["power3"],
#                 'power4': data1["power4"],
#                 'sum_power': data1["sum_power"],
#                 'work_status': data2["work_status"],
#                 'pump_p301_status': data2["pump_p301_status"],
#                 'valve_B1101_status': data2["valve_B1101_status"],
#                 'valve_B1601_status': data2["valve_B1601_status"],
#                 'compres_V501_status': data2["compres_V501_status"],
#                 'compres_V502_status': data2["compres_V502_status"],
#                 'compres_V503_status': data2["compres_V503_status"],
#                 'generator_D601_status1': data2["generator_D601_status1"],
#                 'generator_D601_status2': data2["generator_D601_status2"],
#                 'generator_D602_status1': data2["generator_D602_status1"],
#                 'generator_D602_status2': data2["generator_D602_status2"],
#                 'generator_D603_status1': data2["generator_D603_status1"],
#                 'generator_D603_status2': data2["generator_D603_status2"],
#                 'generator_D604_status1': data2["generator_D604_status1"],
#                 'generator_D604_status2': data2["generator_D604_status2"],
#                 'fakel_A604': data2["fakel_A604"]
#             }