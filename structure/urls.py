from django.urls import path

from .views import Parametrs
from .viewset import *

urlpatterns = [
    path('wizard/step1', Parametrs.step1, name='wizard_sep1'),
    path('get_structure', Parametrs.get_structure,name='get_structure'),

]
