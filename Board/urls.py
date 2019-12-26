from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('Board', views.BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("<int:pk>", views.BoardDetail.as_view()),
]
