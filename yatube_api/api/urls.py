from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentListCreateAPIView, \
    CommentRUDAPIView

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view()),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentRUDAPIView.as_view()),
]
