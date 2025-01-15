from django.urls import path

from apps.users.views import UserCreateView, UserDetailView


urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-list'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),
]
