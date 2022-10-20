from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from auth_sample.models import User
from auth_sample.serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt import views as jwt_views


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = ()

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save()


permission_cls = {"permission_classes": ()}
obtain_jwt_token = jwt_views.TokenObtainPairView.as_view(**permission_cls)
refresh_jwt_token = jwt_views.TokenRefreshView.as_view(**permission_cls)


class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    permission_classes = ()
    serializer_class = MyTokenObtainPairSerializer


