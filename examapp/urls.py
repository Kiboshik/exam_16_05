from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikesViewSet, CommentsViewSet


router = DefaultRouter()


router.register("post", PostViewSet, basename="post")
router.register("like", LikesViewSet, basename="like")
router.register("comment", CommentsViewSet, basename="comment")


urlpatterns = [
    path("",include(router.urls)),
]
