from django.urls import path, include
from rest_framework import routers
from .views import CursViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('curs', CursViewSet) #/api/curs
router.register('student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace="rest_framework"))
]