from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
# from .models import Dog
from .serializers import DogSerializer

from .models import Animal
from .serializers import *


class AnimalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='dog')
    serializer_class = DogSerializer

    def perform_create(self, serializer):
        serializer.save(species='dog')

    # def create(self, request):
    #     serializer = DogSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None):
    #     try:
    #         dog = Animal.objects.get(pk=pk)
    #     except Animal.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = DogSerializer(dog)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None):
    #     try:
    #         dog = Animal.objects.get(pk=pk)
    #     except Animal.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = DogSerializer(dog, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def destroy(self, request, pk=None):
    #     try:
    #         dog = Animal.objects.get(pk=pk)
    #     except Animal.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     dog.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='cat')
    serializer_class = CatSerializer

    def create(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            dog = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            dog = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            dog = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class AnimalImageViewSet(viewsets.ModelViewSet):
    queryset = AnimalImage.objects.all()
    serializer_class = AnimalImageSerializer
