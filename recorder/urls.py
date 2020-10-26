from django.urls import path, include

from recorder.views import Recorder

urlpatterns = [
    path('list/line/', Recorder.as_view()),
]