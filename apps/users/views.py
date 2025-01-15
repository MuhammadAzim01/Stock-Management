from rest_framework import generics
from django.core.cache import cache

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        cache_key = f'user_{username}'
        
        cached_user = cache.get(cache_key)
        if cached_user:
            return cached_user

        user = super().get_object()
        cache.set(cache_key, user, timeout=300)
        return user
