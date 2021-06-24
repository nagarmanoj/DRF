from django.urls import path,include
from rest_framework.routers import DefaultRouter
from blog.api import views

router = DefaultRouter()
router.register('postapi',views.PostModelViewSet,basename="post")
router.register('commentapi',views.CommentModelViewSet,basename="comment")

urlpatterns = [
    path('',include(router.urls))
]
