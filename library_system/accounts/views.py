from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# عرض المستخدمين
class UserListView(generics.ListCreateAPIView):
  
    queryset = User.objects.all()
    serializer_class = UserSerializer

# عرض تفاصيل مستخدم واحد
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

