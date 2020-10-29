import math
import random
from datetime import datetime
import string
from .models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import UserSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            # update the created time of the token to keep it valid
            val = get_random_string(25)
            Token.objects.filter(user=user).update(key=val)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class Logout(APIView):
    def post(self, request, format=None):
        # simply delete the token to force a login
        print(dir(request.user))
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserModelView(APIView):

    def get(self, request, pk):
        a = User.objects.get(pk=pk)
        serializer = UserSerializer(a, many=False)
        return Response({"user": serializer.data})


    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_list(request):
        a = User.objects.all()
        serializer = UserSerializer(a, many=True)
        return Response({"users": serializer.data})

    @api_view(['GET', 'POST', ])
    def getSuperusers(request):
        a = User.objects.filter(is_superuser=True)
        # data = serializers.serialize('json', a)
        # print(data)
        # return HttpResponse(data, content_type="application/json")
        serializer = UserSerializer(a, many=True)
        print(serializer.data)
        return Response(serializer.data)


# preobrazovanie datetimestamp v unix time
def datetimeconverter(o):
    if isinstance(o, datetime.datetime):
        return math.ceil(o.timestamp() * 1000)
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return  result_str
