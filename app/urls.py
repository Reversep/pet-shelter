from django.urls import path, include
from rest_framework import routers

from . import views
#
#
router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'volunteer', views.VolunteerViewSet)
router.register(r'image', views.AnimalImageViewSet)
# router.register(r'dog', views.DogViewSet, basename='dogs')
# router.register(r'cat', views.CatViewSet, basename='cats')


urlpatterns = [

    path('', include(router.urls)),

    path('dog/', views.DogViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('dog/<int:pk>', views.DogViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),

    path('cat/', views.CatViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('cat/<int:pk>', views.CatViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),

]
