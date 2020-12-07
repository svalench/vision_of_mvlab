from dashboard.teldefax_dashboard import TransitionReadings, GenerationOfElectricity, Status
from rest_framework.views import APIView
from rest_framework.response import Response

class teldafax(TransitionReadings, GenerationOfElectricity, Status, APIView):
    """
    Класс для вывода данных для dashboard
    """
    def get(self, request):
        name_dash = self.request.query_params.get('name')
        # условия проверки запроса какой виджет требуется
        if name_dash == "transition_readings":
            # данные для виджета "Показания перехода"
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
            # данные для виджета "Выработка электроэнергии"
            a = {
                "machine1": self.machine1(),
                "machine2": self.machine2(),
                "machine3": self.machine3(),
                "machine4": self.machine4(),
                "sum": self.sum()
            }
        elif name_dash == "mode":
            # данные для виджета "Режим работы"
            a = self.mode()
        elif name_dash == "damper":
            # данные для виджета "Задвижки"
            a = {
                "damper1": self.damper1(),
                "damper2": self.damper2()
            }
        elif name_dash == "pump":
            # данные для виджета "Насосы"
            a = self.pump()
        elif name_dash == "compress":
            # данные для виджета "Компрессоры"
            a = {
                "compress1": self.compress1(),
                "compress2": self.compress2(),
                "compress3": self.compress3()
            }
        elif name_dash == "machine":
            # данные для виджета "Машины"
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