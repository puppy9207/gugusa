from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Portfolio import views

router = DefaultRouter()
router.register('Portfolio', views.PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("<int:pk>", views.PortfolioDetail.as_view()),
]