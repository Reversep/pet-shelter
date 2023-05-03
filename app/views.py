from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import DogSerializer

from .permissions import IsAuthenticatedOrSafeMethods

from .models import Animal
from .serializers import *


class AnimalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]




class DogViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='dog')
    serializer_class = DogSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]

    def perform_create(self, serializer):
        serializer.save(species='dog')



class CatViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='cat')
    serializer_class = CatSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]

    def perform_create(self, serializer):
        serializer.save(species='cat')



class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


class AnimalImageViewSet(viewsets.ModelViewSet):
    queryset = AnimalImage.objects.all()
    serializer_class = AnimalImageSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


@api_view(http_method_names=['GET', ])
@authentication_classes([BasicAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_user_info(request):
    user = request.user
    data = {
        'username': user.username,
        'password': user.password
    }
    return Response(data)