from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from authentication.views import UserViewSet
from api.views import CategoryViewSet, ManufacturerViewSet, ProductViewSet

router = DefaultRouter()
router.register('auth', UserViewSet)
router.register('product', ProductViewSet)
router.register('manufacturer', ManufacturerViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
