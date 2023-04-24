from django.urls import path,include
from .views import JobViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]