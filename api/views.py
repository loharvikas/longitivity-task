from django.shortcuts import render
from rest_framework import generics
from users.models import User
from marketplace.models import Organisation
from .serializers import UserSerializer, OrganisationSerializer
from rest_framework.permissions import AllowAny


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class OrganisationAPIView(generics.ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = (AllowAny,)
