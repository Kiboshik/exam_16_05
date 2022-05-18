from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterAPIViews


urlpatterns = [
    path("register/", UserRegisterAPIViews.as_view()),
    path('login/', obtain_auth_token),
]
