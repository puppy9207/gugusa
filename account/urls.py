from rest_framework.routers import DefaultRouter
from django.urls import path, include
from account import views

router = DefaultRouter()
router.register('account', views.accountViewSet)

urlpatterns = [
    path('', include(router.urls))
]