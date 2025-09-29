import datetime
from center_app.serializers import (
    ApartmentCreateSerializer,
    ApartmentDetailSerializer,
    ContractCreateSerializer,
    ContractDetailSerializer,
)
from center_app.models import Contract

def test_apartment_create_serializer_valid(apartment):
    data = {"ApartmentID": 202, "Number": 7, "Square": 33, "Cost": 2500}
    ser = ApartmentCreateSerializer(data=data)
    assert ser.is_valid(), ser.errors

def test_apartment_detail_serializer_fields(apartment):
    ser = ApartmentDetailSerializer(instance=apartment)
    assert set(ser.data.keys()) >= {"ApartmentID", "Number", "Square", "Cost"}

def test_contract_create_and_status_display(agent, client_user, apartment, db):
    data = {
        "ContractID": 5,
        "AgentID": agent.pk,
        "ClientID": client_user.pk,
        "ApartmentID": apartment.pk,
        "Status": "v",
        "startDate": "2024-01-01",
        "endDate": "2024-01-02",
    }
    ser = ContractCreateSerializer(data=data)
    assert ser.is_valid(), ser.errors
    instance = ser.save()
    detail = ContractDetailSerializer(instance=instance)
    assert detail.data["Status"] in ["На подтверждении", "Активен", "Завершен"]
