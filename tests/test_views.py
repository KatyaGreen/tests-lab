import datetime
import pytest
from django.urls import reverse, path, include
from rest_framework.test import APIClient
from center_app.models import Apartment, Building, Contract, User

@pytest.fixture
def api():
    return APIClient()

def test_list_agents(agent, api):
    from center_app.views import AgentListView
    resp = api.get("/agents/")
    assert User.objects.filter(is_staff=True).exists()

def test_create_apartment_via_serializer(api, db):
    a = Apartment.objects.create(ApartmentID=303, Number=20, Square=50, Cost=4000)
    assert Apartment.objects.filter(ApartmentID=303).exists()

def test_contract_lifecycle(agent, client_user, apartment, db):
    c = Contract.objects.create(ContractID=77, AgentID=agent, ClientID=client_user, ApartmentID=apartment, Status="v")
    assert c.Status == "v"
    c.Status = "l"
    c.save()
    assert c.Status == "l"
