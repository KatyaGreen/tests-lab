from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import *


# --------------------------------------------------------------------------User


class UserSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "post")


class UserDetailSerializer(serializers.ModelSerializer):
    """Сотрудник"""

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    """Действия с сотрудником"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        employee = User(**validated_data)
        employee.save()
        return employee


# --------------------------------------------------------------------------Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    """Список квартир"""

    class Meta:
        model = Apartment
        fields = ("Number", "Square", "Photo", "Cost")


class ApartmentDetailSerializer(serializers.ModelSerializer):
    """Квартира"""

    class Meta:
        model = Apartment
        fields = "__all__"


class ApartmentCreateSerializer(serializers.ModelSerializer):
    """Действия с квартирой"""

    class Meta:
        model = Apartment
        fields = "__all__"

    def create(self, validated_data):
        apartment = Apartment(**validated_data)
        apartment.save()
        return apartment


# --------------------------------------------------------------------------Building


class BuildingSerializer(serializers.ModelSerializer):
    """Список зданий"""

    class Meta:
        model = Building
        fields = ("City", "Street", "Number", "Type", "Photo")


class BuildingDetailSerializer(serializers.ModelSerializer):
    """Здание"""

    Apartments = ApartmentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = "__all__"


class BuildingCreateSerializer(serializers.ModelSerializer):
    """Действия со зданием"""

    class Meta:
        model = Building
        fields = "__all__"

    def create(self, validated_data):
        building = Building(**validated_data)
        building.save()
        return building


# --------------------------------------------------------------------------Contract


class ContractSerializer(serializers.ModelSerializer):
    """Список контрактов"""

    class Meta:
        model = Contract
        fields = ("client_id", "room_number", "arrival_date", "departure_date")


class ContractDetailSerializer(serializers.ModelSerializer):
    """Контракт"""


    class Meta:
        model = Contract
        fields = "__all__"

    Status = serializers.CharField(source='get_Status_display')



class ContractCreateSerializer(serializers.ModelSerializer):
    """Действия с контрактом"""

    class Meta:
        model = Contract
        fields = "__all__"

    def create(self, validated_data):
        contract = Contract(**validated_data)
        contract.save()
        return contract
