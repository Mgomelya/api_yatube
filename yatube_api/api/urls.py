from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentListCreateAPIView, \
    CommentRUDAPIView

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/posts/<int:post_id>/comments/',
         CommentListCreateAPIView.as_view()),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentRUDAPIView.as_view()),
]
