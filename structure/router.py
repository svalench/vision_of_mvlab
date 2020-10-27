from rest_framework import routers

from .viewset import *

router1 = routers.DefaultRouter()

router1.register(r'Corparation', CorparationView)
router1.register(r'Factory', FactoryView)
router1.register(r'Department', DepartmentView)
router1.register(r'Shift', ShiftView)
router1.register(r'Lunch', LunchView)
router1.register(r'Agreagat', AgreagatView)
router1.register(r'Sensors', SensorsView)

# urlpatterns = [
#     path('Corparation/', CorparationView.as_view()),
# ]
#
# urlpatterns += router1.urls