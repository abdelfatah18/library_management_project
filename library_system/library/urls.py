from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  # إضافة basename هنا
router.register(r'transactions', TransactionViewSet, basename='transaction')  # إضافة basename هنا

urlpatterns = [
    path('', include(router.urls)),
]