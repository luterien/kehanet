from django.shortcuts import render

from rest_framework import viewsets

from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


