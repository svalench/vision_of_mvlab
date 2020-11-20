from django.urls import path

from .views import Parametrs
from .viewset import *
from .views import *

urlpatterns = [
    path('wizard/step1', Parametrs.step1, name='wizard_sep1'),
    path('get_structure', Parametrs.get_structure,name='get_structure'),
    path('create/department', Parametrs.create_shift,name='create_dep'),

    path( 'Reserv2/search/<int:pk>/', Reserv2_Search.as_view()),
    path( 'Corparation/search/<int:pk>/', Corparation_Search.as_view()),
    path( 'Company/search/<int:pk>/', Company_Search.as_view()),
    path( 'Factory/search/<int:pk>/', Factory_Search.as_view()),
    path( 'Department/search/<int:pk>/', Department_Search.as_view()),
    path( 'Agreagat/search/<int:pk>/', Agreagat_Search.as_view()),

]
