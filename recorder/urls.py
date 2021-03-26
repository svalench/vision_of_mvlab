from django.urls import path, include

from recorder.views import Recorder, ChartData

urlpatterns = [
    path('list/line/', Recorder.as_view()),
    #path('chart/workarea/', ChartData.as_view()),
]