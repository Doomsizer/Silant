from rest_framework import serializers
from .models import Car, CarModel, EngineModel, TransmissionModel, SubBridgeModel, MainBridgeModel, Maintenance, Reclaim

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'description']

class EngineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineModel
        fields = ['id', 'name', 'description']

class TransmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = ['id', 'name', 'description']

class SubBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubBridgeModel
        fields = ['id', 'name', 'description']

class MainBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBridgeModel
        fields = ['id', 'name', 'description']

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = "__all__"
        depth = 1

class ReclaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclaim
        fields = '__all__'
        depth = 1

class CarSerializer(serializers.ModelSerializer):
    car_model_name = serializers.CharField(source='car_model.name')
    car_model_id = serializers.IntegerField(source='car_model.id', read_only=True)
    engine_model_name = serializers.CharField(source='engine_model.name')
    engine_model_id = serializers.IntegerField(source='engine_model.id', read_only=True)
    trans_model_name = serializers.CharField(source='trans_model.name')
    trans_model_id = serializers.IntegerField(source='trans_model.id', read_only=True)
    main_bridge_model_name = serializers.CharField(source='main_bridge_model.name')
    main_bridge_model_id = serializers.IntegerField(source='main_bridge_model.id', read_only=True)
    sub_bridge_model_name = serializers.CharField(source='sub_bridge_model.name')
    sub_bridge_model_id = serializers.IntegerField(source='sub_bridge_model.id', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    service_company = serializers.CharField(source='service_company.username', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'car_number', 'car_model_name', 'car_model_id', 'engine_model_name', 'engine_model_id',
            'engine_number', 'trans_model_name', 'trans_model_id', 'trans_number', 'main_bridge_model_name',
            'main_bridge_model_id', 'main_bridge_number', 'sub_bridge_model_name', 'sub_bridge_model_id',
            'sub_bridge_number', 'contract_number_date', 'send_date', 'receiver', 'address', 'equipment',
            'user', 'service_company'
        ]
        depth = 1

    def to_representation(self, instance):
        user = self.context.get('user')
        ret = super().to_representation(instance)

        basic_fields = [
            'id', 'car_number', 'car_model_name', 'engine_model_name', 'engine_number',
            'trans_model_name', 'trans_number', 'main_bridge_model_name', 'main_bridge_number',
            'sub_bridge_model_name', 'sub_bridge_number'
        ]

        if not user:
            return {k: ret[k] for k in basic_fields if k in ret}
        elif user.groups.filter(name='Manager').exists():
            return ret
        elif instance.user == user:
            return ret
        elif instance.service_company == user:
            return ret
        else:
            return {k: ret[k] for k in basic_fields if k in ret}