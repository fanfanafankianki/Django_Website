from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TestViewSet

router = routers.DefaultRouter()
router.register('testing', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch_all/', TestViewSet.as_view({'get': 'fetch_all'}), name='fetch_all'),
]