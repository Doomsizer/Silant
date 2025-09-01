from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Accounts.views import UserInfoView
from Main.views import CarViewSet, CarModelViewSet, EngineModelViewSet, TransmissionModelViewSet, SubBridgeModelViewSet, MainBridgeModelViewSet, MaintenanceViewSet, ReclaimViewSet
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'car-models', CarModelViewSet)
router.register(r'engine-models', EngineModelViewSet)
router.register(r'transmission-models', TransmissionModelViewSet)
router.register(r'sub-bridge-models', SubBridgeModelViewSet)
router.register(r'main-bridge-models', MainBridgeModelViewSet)
router.register(r'maintenances', MaintenanceViewSet)
router.register(r'reclaims', ReclaimViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user-info/', UserInfoView.as_view(), name='user-info'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='react_spa'),
]