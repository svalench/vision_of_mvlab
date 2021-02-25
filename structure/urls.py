from django.urls import path

from .views import *
from .viewset import *

urlpatterns = [
    path('wizard/step1/', Parametrs.step1, name='wizard_sep1'),

    path('get_structure/', Parametrs.get_structure,name='get_structure'),
    path('delete_structure/', Parametrs.delete_structure,name='delete_structure'),
    path('create/department/', Parametrs.create_shift,name='create_dep'),

    # path('Reserv_1/', Reserv_1View.as_view()),
    path('Reserv2/search/<int:pk>/', Reserv2_Search.as_view(), name='searchReserv2'),
    path('Corparation/search/<int:pk>/', Corparation_Search.as_view(), name='searchCorparation'),
    path('Company/search/<int:pk>/', Company_Search.as_view(), name='searchCompany'),
    path('Factory/search/<int:pk>/', Factory_Search.as_view(), name='searchFactory'),
    path('Department/search/<int:pk>/', Department_Search.as_view(), name='searchDepartment'),
    path('Agreagat/search/<int:pk>/', Agreagat_Search.as_view(), name='searchAgreagat'),
    path('status/connection/', StatusConnections.as_view()),

]
