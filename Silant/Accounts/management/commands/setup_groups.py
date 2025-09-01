from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from Main.models import Car, Maintenance, Reclaim, CarModel, EngineModel, TransmissionModel, MainBridgeModel, SubBridgeModel, MaintenanceType, MaintenanceOrganisation, ReclaimBrokePlace, ReclaimRestoreMethod

class Command(BaseCommand):
    help = 'Создает группы и разрешения для ролей'

    def handle(self, *args, **kwargs):
        client_group, _ = Group.objects.get_or_create(name='Client')
        service_group, _ = Group.objects.get_or_create(name='ServiceOrganization')
        manager_group, _ = Group.objects.get_or_create(name='Manager')

        car_ct = ContentType.objects.get_for_model(Car)
        maintenance_ct = ContentType.objects.get_for_model(Maintenance)
        reclaim_ct = ContentType.objects.get_for_model(Reclaim)
        car_model_ct = ContentType.objects.get_for_model(CarModel)
        engine_model_ct = ContentType.objects.get_for_model(EngineModel)
        transmission_model_ct = ContentType.objects.get_for_model(TransmissionModel)
        main_bridge_model_ct = ContentType.objects.get_for_model(MainBridgeModel)
        sub_bridge_model_ct = ContentType.objects.get_for_model(SubBridgeModel)
        maintenance_type_ct = ContentType.objects.get_for_model(MaintenanceType)
        maintenance_organisation_ct = ContentType.objects.get_for_model(MaintenanceOrganisation)
        reclaim_broke_place_ct = ContentType.objects.get_for_model(ReclaimBrokePlace)
        reclaim_restore_method_ct = ContentType.objects.get_for_model(ReclaimRestoreMethod)

        view_car, _ = Permission.objects.get_or_create(codename='view_car', defaults={'name': 'Can view car'}, content_type=car_ct)
        add_car, _ = Permission.objects.get_or_create(codename='add_car', defaults={'name': 'Can add car'}, content_type=car_ct)
        change_car, _ = Permission.objects.get_or_create(codename='change_car', defaults={'name': 'Can change car'}, content_type=car_ct)

        view_maintenance, _ = Permission.objects.get_or_create(codename='view_maintenance', defaults={'name': 'Can view maintenance'}, content_type=maintenance_ct)
        add_maintenance, _ = Permission.objects.get_or_create(codename='add_maintenance', defaults={'name': 'Can add maintenance'}, content_type=maintenance_ct)
        change_maintenance, _ = Permission.objects.get_or_create(codename='change_maintenance', defaults={'name': 'Can change maintenance'}, content_type=maintenance_ct)

        view_reclaim, _ = Permission.objects.get_or_create(codename='view_reclaim', defaults={'name': 'Can view reclaim'}, content_type=reclaim_ct)
        add_reclaim, _ = Permission.objects.get_or_create(codename='add_reclaim', defaults={'name': 'Can add reclaim'}, content_type=reclaim_ct)
        change_reclaim, _ = Permission.objects.get_or_create(codename='change_reclaim', defaults={'name': 'Can change reclaim'}, content_type=reclaim_ct)

        view_car_model, _ = Permission.objects.get_or_create(codename='view_carmodel', defaults={'name': 'Can view car model'}, content_type=car_model_ct)
        add_car_model, _ = Permission.objects.get_or_create(codename='add_carmodel', defaults={'name': 'Can add car model'}, content_type=car_model_ct)
        change_car_model, _ = Permission.objects.get_or_create(codename='change_carmodel', defaults={'name': 'Can change car model'}, content_type=car_model_ct)

        view_engine_model, _ = Permission.objects.get_or_create(codename='view_enginemodel', defaults={'name': 'Can view engine model'}, content_type=engine_model_ct)
        add_engine_model, _ = Permission.objects.get_or_create(codename='add_enginemodel', defaults={'name': 'Can add engine model'}, content_type=engine_model_ct)
        change_engine_model, _ = Permission.objects.get_or_create(codename='change_enginemodel', defaults={'name': 'Can change engine model'}, content_type=engine_model_ct)

        view_transmission_model, _ = Permission.objects.get_or_create(codename='view_transmissionmodel', defaults={'name': 'Can view transmission model'}, content_type=transmission_model_ct)
        add_transmission_model, _ = Permission.objects.get_or_create(codename='add_transmissionmodel', defaults={'name': 'Can add transmission model'}, content_type=transmission_model_ct)
        change_transmission_model, _ = Permission.objects.get_or_create(codename='change_transmissionmodel', defaults={'name': 'Can change transmission model'}, content_type=transmission_model_ct)

        view_main_bridge_model, _ = Permission.objects.get_or_create(codename='view_mainbridgemodel', defaults={'name': 'Can view main bridge model'}, content_type=main_bridge_model_ct)
        add_main_bridge_model, _ = Permission.objects.get_or_create(codename='add_mainbridgemodel', defaults={'name': 'Can add main bridge model'}, content_type=main_bridge_model_ct)
        change_main_bridge_model, _ = Permission.objects.get_or_create(codename='change_mainbridgemodel', defaults={'name': 'Can change main bridge model'}, content_type=main_bridge_model_ct)

        view_sub_bridge_model, _ = Permission.objects.get_or_create(codename='view_subbridgemodel', defaults={'name': 'Can view sub bridge model'}, content_type=sub_bridge_model_ct)
        add_sub_bridge_model, _ = Permission.objects.get_or_create(codename='add_subbridgemodel', defaults={'name': 'Can add sub bridge model'}, content_type=sub_bridge_model_ct)
        change_sub_bridge_model, _ = Permission.objects.get_or_create(codename='change_subbridgemodel', defaults={'name': 'Can change sub bridge model'}, content_type=sub_bridge_model_ct)

        view_maintenance_type, _ = Permission.objects.get_or_create(codename='view_maintenancetype', defaults={'name': 'Can view maintenance type'}, content_type=maintenance_type_ct)
        add_maintenance_type, _ = Permission.objects.get_or_create(codename='add_maintenancetype', defaults={'name': 'Can add maintenance type'}, content_type=maintenance_type_ct)
        change_maintenance_type, _ = Permission.objects.get_or_create(codename='change_maintenancetype', defaults={'name': 'Can change maintenance type'}, content_type=maintenance_type_ct)

        view_maintenance_organisation, _ = Permission.objects.get_or_create(codename='view_maintenanceorganisation', defaults={'name': 'Can view maintenance organisation'}, content_type=maintenance_organisation_ct)
        add_maintenance_organisation, _ = Permission.objects.get_or_create(codename='add_maintenanceorganisation', defaults={'name': 'Can add maintenance organisation'}, content_type=maintenance_organisation_ct)
        change_maintenance_organisation, _ = Permission.objects.get_or_create(codename='change_maintenanceorganisation', defaults={'name': 'Can change maintenance organisation'}, content_type=maintenance_organisation_ct)

        view_reclaim_broke_place, _ = Permission.objects.get_or_create(codename='view_reclaimbrokeplace', defaults={'name': 'Can view reclaim broke place'}, content_type=reclaim_broke_place_ct)
        add_reclaim_broke_place, _ = Permission.objects.get_or_create(codename='add_reclaimbrokeplace', defaults={'name': 'Can add reclaim broke place'}, content_type=reclaim_broke_place_ct)
        change_reclaim_broke_place, _ = Permission.objects.get_or_create(codename='change_reclaimbrokeplace', defaults={'name': 'Can change reclaim broke place'}, content_type=reclaim_broke_place_ct)

        view_reclaim_restore_method, _ = Permission.objects.get_or_create(codename='view_reclaimrestoremethod', defaults={'name': 'Can view reclaim restore method'}, content_type=reclaim_restore_method_ct)
        add_reclaim_restore_method, _ = Permission.objects.get_or_create(codename='add_reclaimrestoremethod', defaults={'name': 'Can add reclaim restore method'}, content_type=reclaim_restore_method_ct)
        change_reclaim_restore_method, _ = Permission.objects.get_or_create(codename='change_reclaimrestoremethod', defaults={'name': 'Can change reclaim restore method'}, content_type=reclaim_restore_method_ct)

        client_group.permissions.add(view_car, view_maintenance, add_maintenance, change_maintenance, view_reclaim, view_car_model, view_engine_model, view_transmission_model, view_main_bridge_model, view_sub_bridge_model, view_maintenance_type, view_maintenance_organisation, view_reclaim_broke_place, view_reclaim_restore_method)

        service_group.permissions.add(view_car, view_maintenance, add_maintenance, change_maintenance, view_reclaim, add_reclaim, change_reclaim, view_car_model, view_engine_model, view_transmission_model, view_main_bridge_model, view_sub_bridge_model, view_maintenance_type, view_maintenance_organisation, view_reclaim_broke_place, view_reclaim_restore_method)

        manager_group.permissions.add(
            view_car, add_car, change_car,
            view_maintenance, add_maintenance, change_maintenance,
            view_reclaim, add_reclaim, change_reclaim,
            view_car_model, add_car_model, change_car_model,
            view_engine_model, add_engine_model, change_engine_model,
            view_transmission_model, add_transmission_model, change_transmission_model,
            view_main_bridge_model, add_main_bridge_model, change_main_bridge_model,
            view_sub_bridge_model, add_sub_bridge_model, change_sub_bridge_model,
            view_maintenance_type, add_maintenance_type, change_maintenance_type,
            view_maintenance_organisation, add_maintenance_organisation, change_maintenance_organisation,
            view_reclaim_broke_place, add_reclaim_broke_place, change_reclaim_broke_place,
            view_reclaim_restore_method, add_reclaim_restore_method, change_reclaim_restore_method
        )

        self.stdout.write(self.style.SUCCESS('Группы и разрешения успешно созданы'))