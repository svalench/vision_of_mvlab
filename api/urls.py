from django.urls import path, include
from django.urls import path, register_converter
from datetime import datetime
from dashboard.viewset import *


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'yyyy')

urlpatterns = [
    # path('', DurationViews.as_view()),
    path('date/', DateViews.as_view()),
    path('duration/<yyyy:date>/day/', DurationViews.as_view()),
    # path('duration/<yyyy:date>/shift/<int:id>/',),*
    path('remainder/<yyyy:date>/',RemainderViews.as_view()),
    # path('edition/<yyyy:date>/month/',),*
    path('edition/<yyyy:date>/day/',EditionViews.as_view()),
    # path('edition/<yyyy:date>/shift/<int:id>/',),*
    # path('sumexpense/<yyyy:date>/month/',),*
    path('sumexpense/<yyyy:date>/day/',SumexpenseDayViews.as_view()),
    # path('sumexpense/<yyyy:date>/shift/<int:id>/',),*
    # path('energyconsumption/<yyyy:date>/month/',),*
    path('energyconsumption/<yyyy:date>/day/',EnergyConsumptionDayViews.as_view()),
    # path('energyconsumption/<yyyy:date>/shift/<int:id>/',),*
    # path('specificconsumption/<yyyy:date>/month/',),*
    path('specificconsumption/<yyyy:date>/day/',SpecificConsumptionDayViews.as_view()),
    # path('specificconsumption/<yyyy:date>/shift/<int:id>/',),*
    # path('comparison/month/<yyyy:date1>/<yyyy:date2>/',),
    path('comparison/day/<yyyy:date1>/<yyyy:date2>/',ComparisonViews.as_view()),
    # path('comparison/shift/<yyyy:date1>/<int:id1>/<yyyy:date2>/<int:id2>/',),

]
