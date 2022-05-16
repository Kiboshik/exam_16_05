from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, LikesViewSet, CommentsViewSet, UserRegisterAPIViews


router = DefaultRouter()


router.register("post", PostViewSet, basename="post")
router.register("like", LikesViewSet, basename="like")
router.register("comment", CommentsViewSet, basename="comment")


urlpatterns = [
    path("",include(router.urls)),
    path("register/", UserRegisterAPIViews.as_view()),
    path('login/', obtain_auth_token),
]
