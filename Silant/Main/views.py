from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Car, CarModel, EngineModel, TransmissionModel, SubBridgeModel, MainBridgeModel, Maintenance, Reclaim
from .serializers import CarSerializer, CarModelSerializer, EngineModelSerializer, TransmissionModelSerializer, \
    MainBridgeModelSerializer, MaintenanceSerializer, ReclaimSerializer, SubBridgeModelSerializer
from Accounts.permissions import CanViewCar, CanEditCar
from Accounts.models import CustomUser

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().select_related('car_model', 'engine_model', 'trans_model', 'main_bridge_model', 'sub_bridge_model', 'user', 'service_company')
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [CanEditCar()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = self.queryset
        user = getattr(self.request, 'user', None) if hasattr(self, 'request') else None
        car_number = self.request.query_params.get('car_number')
        if car_number:
            queryset = queryset.filter(car_number=car_number)
        elif user:
            if user.groups.filter(name='Client').exists():
                queryset = queryset.filter(user=user)
            elif user.groups.filter(name='ServiceOrganization').exists():
                queryset = queryset.filter(service_company=user)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = getattr(self.request, 'user', None) if hasattr(self, 'request') else None
        context['request'] = self.request
        context['user'] = user
        return context

class CarModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsAuthenticated]

class EngineModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer
    permission_classes = [IsAuthenticated]

class TransmissionModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer
    permission_classes = [IsAuthenticated]

class SubBridgeModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubBridgeModel.objects.all()
    serializer_class = SubBridgeModelSerializer
    permission_classes = [IsAuthenticated]

class MainBridgeModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainBridgeModel.objects.all()
    serializer_class = MainBridgeModelSerializer
    permission_classes = [IsAuthenticated]

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all().select_related('type', 'car', 'service_company')
    serializer_class = MaintenanceSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [CanEditCar()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = getattr(self.request, 'user', None) if hasattr(self, 'request') else None
        car_id = self.request.query_params.get('car')
        if car_id:
            queryset = queryset.filter(car__id=car_id)
        elif user:
            if user.groups.filter(name='Client').exists():
                queryset = queryset.filter(car__user=user)
            elif user.groups.filter(name='ServiceOrganization').exists():
                queryset = queryset.filter(car__service_company=user)
        return queryset

class ReclaimViewSet(viewsets.ModelViewSet):
    queryset = Reclaim.objects.all().select_related('broke_place', 'restore_method', 'car', 'service_company')
    serializer_class = ReclaimSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [CanEditCar()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = getattr(self.request, 'user', None) if hasattr(self, 'request') else None
        car_id = self.request.query_params.get('car')
        if car_id:
            queryset = queryset.filter(car__id=car_id)
        elif user:
            if user.groups.filter(name='Client').exists():
                queryset = queryset.filter(car__user=user)
            elif user.groups.filter(name='ServiceOrganization').exists():
                queryset = queryset.filter(car__service_company=user)
        return queryset