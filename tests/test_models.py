import datetime
from django.db import IntegrityError
from center_app.models import Contract
from pytest import raises

def test_user_fields_defaults(agent):
    assert agent.username == "agent"
    assert hasattr(agent, "Passport")
    assert hasattr(agent, "Phone")
    assert hasattr(agent, "BirthDate")
    assert hasattr(agent, "Photo")

def test_apartment_core_fields(apartment):
    assert apartment.ApartmentID == 101
    assert apartment.Number == 12
    assert apartment.Square == 45
    assert apartment.Cost == 3000

def test_building_m2m_apartments(building, apartment):
    assert apartment in building.Apartments.all()

def test_contract_status_choices(agent, client_user, apartment, db):
    c = Contract.objects.create(
        ContractID=1,
        AgentID=agent,
        ClientID=client_user,
        ApartmentID=apartment,
        Status="v",
        startDate=datetime.date(2024, 1, 1),
        endDate=datetime.date(2024, 1, 10),
    )
    assert c.get_Status_display() == "На подтверждении"
    c.Status = "l"
    c.save(update_fields=["Status"])
    assert c.get_Status_display() == "Активен"

def test_contract_unique_pk(db, agent, client_user, apartment):
    from center_app.models import Contract
    Contract.objects.create(ContractID=10, AgentID=agent, ClientID=client_user, ApartmentID=apartment, Status="v")
    with raises(IntegrityError):
        Contract.objects.create(ContractID=10, AgentID=agent, ClientID=client_user, ApartmentID=apartment, Status="v")
