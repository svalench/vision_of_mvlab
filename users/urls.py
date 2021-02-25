from django.urls import path, include

from users.views import CustomAuthToken, Logout, UserData

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name="login_link"),
    path('logout/', Logout.as_view()),
    path('myname/',UserData.as_view({"get":"retrieve"}))
]
