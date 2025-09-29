import os
import django
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "center_project.settings")
django.setup()

from django.contrib.auth import get_user_model
from center_app.models import Apartment, Building, Contract

@pytest.fixture
def User():
    return get_user_model()

@pytest.fixture
def agent(User, db):
    return User.objects.create_user(username="agent", password="pwd", is_staff=True, first_name="A", last_name="G")

@pytest.fixture
def client_user(User, db):
    return User.objects.create_user(username="client", password="pwd", is_staff=False, first_name="C", last_name="L")

@pytest.fixture
def apartment(db):
    return Apartment.objects.create(ApartmentID=101, Number=12, Square=45, Cost=3000)

@pytest.fixture
def building(db, apartment):
    b = Building.objects.create(BuildingID=1, City="SPB", Street="Nevsky", Number="1", Type="brick")
    b.Apartments.add(apartment)
    return b
