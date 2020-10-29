from users.models import UserP
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from api.serializer import UserSerializer


@permission_classes([IsAdminUser])
class UserList(viewsets.ModelViewSet):
    queryset = UserP.objects.all()
    serializer_class = UserSerializer