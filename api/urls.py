from django.urls import path, include
from django.urls import path, register_converter
from datetime import datetime
from dashboard.viewset import *
from api.views_teldafax import teldafax, Teldafax_status, GetStatusConnectionsTeldafax, \
    TeldafaxErrorTablesAndStatusInIt, GetConnectionsTeldafax, GetConnectionsVariablesTeldafax


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('duration/<yyyy:date>/day/', DurationIntervalDayViews.as_view(), name="duration_day"),
    path('duration/<yyyy:date>/shift/<int:id>/', DurationIntervalShiftViews.as_view(), name="duration_shift"),
    path('remainder/<yyyy:date>/', RemainderViews.as_view(), name='remainder'),
    path('edition/<yyyy:date>/month/', EditionMonthViews.as_view(), name='edition_month'),
    path('edition/<yyyy:date>/day/', EditionDayViews.as_view(), name='edition_day'),
    path('edition/<yyyy:date>/shift/<int:id>/', EditionShiftViews.as_view(), name='edition_shift'),
    path('sumexpense/<yyyy:date>/month/', SumexpenseMonthViews.as_view(), name='sumexpense_month'),
    path('sumexpense/<yyyy:date>/day/', SumexpenseDayViews.as_view(), name='sumexpense_day'),
    path('sumexpense/<yyyy:date>/shift/<int:id>/', SumexpenseShiftViews.as_view(), name='sumexpense_shift'),
    path('energyconsumption/<yyyy:date>/month/', EnergyConsumptionMonthViews.as_view(), name='energyconsumption_month'),
    path('energyconsumption/<yyyy:date>/day/', EnergyConsumptionDayViews.as_view(), name='energyconsumption_day'),
    path('energyconsumption/<yyyy:date>/shift/<int:id>/', EnergyConsumptionShiftViews.as_view(), name='energyconsumption_shift'),
    path('specificconsumption/<yyyy:date>/month/', SpecificConsumptionMonthViews.as_view(), name='specificconsumption_month'),
    path('specificconsumption/<yyyy:date>/day/', SpecificConsumptionDayViews.as_view(), name='specificconsumption_day'),
    path('specificconsumption/<yyyy:date>/shift/<int:id>/', SpecificConsumptionShiftViews.as_view(), name='specificconsumption_shift'),
    path('comparison/month/<yyyy:date1>/<yyyy:date2>/', ComparisonMonthViews.as_view(), name='comparison_month'),
    path('comparison/day/<yyyy:date1>/<yyyy:date2>/', ComparisonDayViews.as_view(), name='comparison_day'),
    path('comparison/shift/<yyyy:date1>/<int:id1>/<yyyy:date2>/<int:id2>/', ComparisonShiftViews.as_view(), name='comparison_shift'),
    path('teldafax/value/', teldafax.as_view(), name='teldafax_value'),
    path('teldafax/status/', Teldafax_status.as_view(), name='teldafax_status'),


    path('user/', RoleViews.as_view())

]
