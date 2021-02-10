from rest_framework import routers

from api.viewset import UserList

router = routers.DefaultRouter()

router.register(r'Users', UserList)