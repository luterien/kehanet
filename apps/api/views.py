from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email', 'id',)

@api_view(['POST'])
def register_user(request):
    serialized = ProfileSerializer(data=request.DATA)
    print serialized
    print request.DATA
    if serialized.is_valid():
        p=Profile()
        p.email = serialized.init_data["email"]
        p.username = serialized.init_data["username"]
        p.set_password(serialized.init_data["password"])
        p.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

