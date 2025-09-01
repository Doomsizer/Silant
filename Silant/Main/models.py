from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Accounts.models import CustomUser

class CarModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название модели")
    description = models.TextField(blank=True, verbose_name="Описание модели")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"

class EngineModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название модели двигателя")
    description = models.TextField(blank=True, verbose_name="Описание модели двигателя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель двигателя"
        verbose_name_plural = "Модели двигателей"

class TransmissionModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название модели трансмиссии")
    description = models.TextField(blank=True, verbose_name="Описание модели трансмиссии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель трансмиссии"
        verbose_name_plural = "Модели трансмиссий"

class MainBridgeModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название модели ведущего моста")
    description = models.TextField(blank=True, verbose_name="Описание модели ведущего моста")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель ведущего моста"
        verbose_name_plural = "Модели ведущих мостов"

class SubBridgeModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название модели управляемого моста")
    description = models.TextField(blank=True, verbose_name="Описание модели управляемого моста")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель управляемого моста"
        verbose_name_plural = "Модели управляемых мостов"

class MaintenanceType(models.Model):
    name = models.CharField(max_length=252, unique=True, verbose_name="Вид ТО")
    description = models.TextField(blank=True, verbose_name="Описание вида ТО")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид ТО"
        verbose_name_plural = "Виды ТО"

class MaintenanceOrganisation(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Организация ТО")
    description = models.TextField(blank=True, verbose_name="Описание организации ТО")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация ТО"
        verbose_name_plural = "Организации ТО"

class ReclaimBrokePlace(models.Model):
    name = models.CharField(max_length=252, unique=True, verbose_name="Узел отказа")
    description = models.TextField(blank=True, verbose_name="Описание узла отказа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Узел отказа"
        verbose_name_plural = "Узлы отказа"

class ReclaimRestoreMethod(models.Model):
    name = models.CharField(max_length=252, unique=True, verbose_name="Способ восстановления")
    description = models.TextField(blank=True, verbose_name="Описание способа восстановления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ восстановления"
        verbose_name_plural = "Способы восстановления"

class Car(models.Model):
    car_number = models.CharField(max_length=252, unique=True, verbose_name="Заводской № машины")
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name="Модель машины")
    engine_model = models.ForeignKey(EngineModel, on_delete=models.PROTECT, verbose_name="Модель двигателя")
    engine_number = models.CharField(max_length=252, verbose_name="Заводской № двигателя")
    trans_model = models.ForeignKey(TransmissionModel, on_delete=models.PROTECT, verbose_name="Модель трансмиссии")
    trans_number = models.CharField(max_length=252, verbose_name="Заводской № трансмиссии")
    main_bridge_model = models.ForeignKey(MainBridgeModel, on_delete=models.PROTECT, verbose_name="Модель ведущего моста")
    main_bridge_number = models.CharField(max_length=252, verbose_name="Заводской № ведущего моста")
    sub_bridge_model = models.ForeignKey(SubBridgeModel, on_delete=models.PROTECT, verbose_name="Модель управляемого моста")
    sub_bridge_number = models.CharField(max_length=252, verbose_name="Заводской № управляемого моста")
    contract_number_date = models.CharField(max_length=252, verbose_name="Договор поставки: №, дата")
    send_date = models.DateField(verbose_name="Дата отгрузки с завода")
    receiver = models.CharField(max_length=50, verbose_name="Грузополучатель")
    address = models.CharField(max_length=50, verbose_name="Адрес поставки")
    equipment = models.TextField(max_length=504, verbose_name="Комплектация (доп. опции)")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'Client'}, verbose_name="Владелец (клиент)")
    service_company = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'ServiceOrganization'}, related_name='serviced_cars', verbose_name="Сервисная компания")

    def __str__(self):
        return f"{self.car_model.name} ({self.car_number})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Maintenance(models.Model):
    type = models.ForeignKey(MaintenanceType, on_delete=models.PROTECT, verbose_name="Вид ТО")
    maintenance_date = models.DateField(verbose_name="Дата проведения ТО")
    worked_for = models.IntegerField(verbose_name="Наработка, м/час")
    order_number = models.CharField(max_length=252, verbose_name="№ заказ-наряда")
    order_date = models.DateField(verbose_name="Дата заказ-наряда")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина")
    service_company = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'ServiceOrganization'}, verbose_name="Сервисная компания")

    def __str__(self):
        return f"{self.type.name} для {self.car} от {self.maintenance_date}"

    class Meta:
        verbose_name = "Техническое обслуживание"
        verbose_name_plural = "Технические обслуживания"

class Reclaim(models.Model):
    broke_date = models.DateField(verbose_name="Дата отказа")
    worked_for = models.IntegerField(verbose_name="Наработка, м/час")
    broke_place = models.ForeignKey(ReclaimBrokePlace, on_delete=models.PROTECT, verbose_name="Узел отказа")
    broke_description = models.TextField(max_length=504, verbose_name="Описание отказа")
    restore_method = models.ForeignKey(ReclaimRestoreMethod, on_delete=models.PROTECT, verbose_name="Способ восстановления")
    used_spare_parts = models.TextField(max_length=252, blank=True, verbose_name="Используемые запасные части")
    restore_date = models.DateField(verbose_name="Дата восстановления")
    downtime = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)], editable=False, verbose_name="Время простоя техники")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина")
    service_company = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'ServiceOrganization'}, verbose_name="Сервисная компания")

    def save(self, *args, **kwargs):
        self.downtime = (self.restore_date - self.broke_date).days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Рекламация для {self.car} от {self.broke_date}"

    class Meta:
        verbose_name = "Рекламация"
        verbose_name_plural = "Рекламации"