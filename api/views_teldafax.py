from dashboard.teldefax_dashboard import TransitionReadings, GenerationOfElectricity, Status
from rest_framework.views import APIView
from rest_framework.response import Response

class teldafax(TransitionReadings, GenerationOfElectricity, Status, APIView):
    def get(self, request):
        name_dash = self.request.query_params.get('name')
        if name_dash == "transition_readings":
            a = {
                "methane": self.methane(),
                "carbondioxide": self.carbondioxide(),
                "oxygen": self.oxygen(),
                "pressure_in": self.pressure_in(),
                "pressure_out": self.pressure_out(),
                "consumption": self.consumption(),
                "temperature": self.temperature()
            }
        elif name_dash == "generation_of_electricity":
            a = {
                "machine1": self.machine1(),
                "machine2": self.machine2(),
                "machine3": self.machine3(),
                "machine4": self.machine4(),
                "sum": self.sum()
            }
        elif name_dash == "mode":
            a = self.mode()
        elif name_dash == "damper":
            a = {
                "damper1": self.damper1(),
                "damper2": self.damper2()
            }
        elif name_dash == "pump":
            a = self.pump()
        elif name_dash == "compress":
            a = {
                "compress1": self.compress1(),
                "compress2": self.compress2(),
                "compress3": self.compress3()
            }
        elif name_dash == "machine":
            a = {
                "generator1": self.generator1(),
                "generator2": self.generator2(),
                "generator3": self.generator3(),
                "generator4": self.generator4(),
                "torch": self.torch()
            }
        else:
            a = "не найден"
        return Response(a)