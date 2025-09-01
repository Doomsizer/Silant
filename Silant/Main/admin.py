from django.contrib import admin
from .models import Car, CarModel, EngineModel, TransmissionModel, SubBridgeModel, MainBridgeModel, MaintenanceType, MaintenanceOrganisation, ReclaimBrokePlace, ReclaimRestoreMethod, Maintenance, Reclaim
from Accounts.models import CustomUser

admin.site.register(CarModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(SubBridgeModel)
admin.site.register(MainBridgeModel)
admin.site.register(MaintenanceType)
admin.site.register(MaintenanceOrganisation)
admin.site.register(ReclaimBrokePlace)
admin.site.register(ReclaimRestoreMethod)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'car_model', 'engine_model', 'user', 'service_company')
    list_filter = ('car_model', 'engine_model', 'user__groups', 'service_company__groups')
    search_fields = ('car_number', 'engine_number', 'trans_number')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.filter(groups__name='Client')
        elif db_field.name == "service_company":
            kwargs["queryset"] = CustomUser.objects.filter(groups__name='ServiceOrganization')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('type', 'maintenance_date', 'car', 'service_company')
    list_filter = ('type', 'service_company__groups')
    search_fields = ('order_number',)

@admin.register(Reclaim)
class ReclaimAdmin(admin.ModelAdmin):
    list_display = ('broke_date', 'car', 'service_company')
    list_filter = ('broke_place', 'restore_method', 'service_company__groups')
    search_fields = ('used_spare_parts',)