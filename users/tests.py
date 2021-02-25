
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from api.viewset import UserList
from users.models import UserP

factory = APIRequestFactory()


class CreateUserTest(APITestCase):
    def setUp(self):
        self.superuser = UserP.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.token, created = Token.objects.get_or_create(user=self.superuser)
        self.token.save()
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson1', 'password': '2222'}

    def test_can_create_user(self):
        request = factory.post('/api/Users', data=self.data, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = UserList.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.superuser = UserP.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.token, created = Token.objects.get_or_create(user=self.superuser)
        self.token.save()
        self.user = UserP.objects.create(username="mike")

    def test_can_read_user_list(self):
        request = factory.get('/api/Users', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = UserList.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        request = factory.get('/api/Users', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.superuser)
        view = UserList.as_view({'get': 'list'})
        response = view(request, args=[self.user.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
