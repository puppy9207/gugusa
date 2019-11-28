from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Project import views

router = DefaultRouter()
router.register('project', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]