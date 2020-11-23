from rest_framework import routers
from .viewset import *

router_recorder = routers.DefaultRouter()


router_recorder.register(r'Workspace', WorkspaceView)
router_recorder.register(r'Workarea', WorkareaView)
router_recorder.register(r'ValueSensor', ValueSensorView)