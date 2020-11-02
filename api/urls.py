from django.urls import path, include
from django.urls import path, register_converter
from datetime import datetime


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('dashboard/prodrab/<yyyy:date>/mesyac/',),
    path('dashboard/prodrab/<yyyy:date>/cutki/',),
    path('dashboard/prodrab/<yyyy:date>/smena/<int:id>/',),
    path('dashboard/ostat/<yyyy:date>/',),
    path('dashboard/vipusk/<yyyy:date>/mesyac/',),
    path('dashboard/vipusk/<yyyy:date>/cutki/',),
    path('dashboard/vipusk/<yyyy:date>/smena/<int:id>/',),
    path('dashboard/sumar_rashod/<yyyy:date>/mesyac/',),
    path('dashboard/sumar_rashod/<yyyy:date>/cutki/',),
    path('dashboard/sumar_rashod/<yyyy:date>/smena/<int:id>/',),
    path('dashboard/rashod_energores/<yyyy:date>/mesyac/',),
    path('dashboard/rashod_energores/<yyyy:date>/cutki/',),
    path('dashboard/rashod_energores/<yyyy:date>/smena/<int:id>/',),
    path('dashboard/ydel_rashod/<yyyy:date>/mesyac/',),
    path('dashboard/ydel_rashod/<yyyy:date>/cutki/',),
    path('dashboard/ydel_rashod/<yyyy:date>/smena/<int:id>/',),
    path('dashboard/modul_sravn/mesyac/<yyyy:date1>/<yyyy:date2>/',),
    path('dashboard/modul_sravn/cutki/<yyyy:date1>/<yyyy:date2>/',),
    path('dashboard/modul_sravn/smena/<yyyy:date1>/<int:id1>/<yyyy:date2>/<int:id2>/',),

]
