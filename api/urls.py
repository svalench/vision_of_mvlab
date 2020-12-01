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
    path('duration/<yyyy:date>/day/', DurationIntervalDayViews.as_view()),
    path('duration/<yyyy:date>/shift/<int:id>/', DurationIntervalShiftViews.as_view()),
    path('remainder/<yyyy:date>/', RemainderViews.as_view()),
    path('edition/<yyyy:date>/month/', EditionMonthViews.as_view()),
    path('edition/<yyyy:date>/day/', EditionDayViews.as_view()),
    path('edition/<yyyy:date>/shift/<int:id>/', EditionShiftViews.as_view()),
    path('sumexpense/<yyyy:date>/month/', SumexpenseMonthViews.as_view()),
    path('sumexpense/<yyyy:date>/day/', SumexpenseDayViews.as_view()),
    path('sumexpense/<yyyy:date>/shift/<int:id>/', SumexpenseShiftViews.as_view()),
    path('energyconsumption/<yyyy:date>/month/', EnergyConsumptionMonthViews.as_view()),
    path('energyconsumption/<yyyy:date>/day/', EnergyConsumptionDayViews.as_view()),
    path('energyconsumption/<yyyy:date>/shift/<int:id>/', EnergyConsumptionShiftViews.as_view()),
    path('specificconsumption/<yyyy:date>/month/', SpecificConsumptionMonthViews.as_view()),
    path('specificconsumption/<yyyy:date>/day/', SpecificConsumptionDayViews.as_view()),
    path('specificconsumption/<yyyy:date>/shift/<int:id>/', SpecificConsumptionShiftViews.as_view()),
    path('comparison/month/<yyyy:date1>/<yyyy:date2>/', ComparisonMonthViews.as_view()),
    path('comparison/day/<yyyy:date1>/<yyyy:date2>/', ComparisonDayViews.as_view()),
    path('comparison/shift/<yyyy:date1>/<int:id1>/<yyyy:date2>/<int:id2>/', ComparisonShiftViews.as_view()),

]
