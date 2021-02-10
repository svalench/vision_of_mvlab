from django.urls import path, include

from users.views import CustomAuthToken, Logout

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('logout/', Logout.as_view()),
]