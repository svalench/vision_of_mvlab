from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.serializer import UserSerializer

@permission_classes([IsAuthenticated])
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer