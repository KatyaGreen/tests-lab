from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """описание пользователя"""
    UserID = models.BigAutoField(primary_key=True, auto_created=True)
    Passport = models.CharField(max_length=100, verbose_name='Паспорт клиента', null=True, blank=True)
    Phone = models.CharField(max_length=11, verbose_name='Телефон для связи с клиентом', null=True, blank=True)
    BirthDate = models.DateField(null=True, blank=True)
    Photo = models.ImageField(verbose_name='Изображение', null=True, blank=True)


class Apartment(models.Model):
    """описание квартиры для продажи"""
    ApartmentID = models.IntegerField(primary_key=True, verbose_name='Идентификатор')
    Number = models.IntegerField(verbose_name='Номер квартиры')
    Square = models.IntegerField(verbose_name='Общая площадь квартиры')
    Description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    Photo = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    Cost = models.IntegerField(verbose_name='Суточная стоимость квартиры')


class Building(models.Model):
    """описание здания для продажи"""
    BuildingID = models.IntegerField(primary_key=True, verbose_name='Идентификатор')
    City = models.CharField(max_length=100, verbose_name='Город')
    Street = models.CharField(max_length=100, verbose_name='Улица')
    Number = models.CharField(max_length=100, verbose_name='Номер дома')
    Type = models.CharField(max_length=100, verbose_name='Тип дома', null=True, blank=True)
    Description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    Photo = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    Apartments = models.ManyToManyField(Apartment, null=True, blank=True, verbose_name="Квартиры",
                                     related_name="apartments")


class Contract(models.Model):
    """описание договора продажи"""
    status_types = (
        ('v', 'На подтверждении'),
        ('l', 'Активен'),
        ('f', 'Завершен')
    )
    ContractID = models.IntegerField(primary_key=True, verbose_name='Регистрационный номер договора')
    AgentID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_agent_id',
                                verbose_name='Идентификационный номер агента')
    ClientID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_client_id',
                                 verbose_name='Регистрационный номер клиента')
    ApartmentID = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Идентификатор квартиры')
    Status = models.CharField(max_length=1, choices=status_types, default='v', verbose_name='Статус')
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)