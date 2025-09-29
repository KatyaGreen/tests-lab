from rest_framework import generics, permissions, status
from django.shortcuts import render
from django.urls import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# --------------------------------------------------------------------------Apartment


class ApartmentListView(generics.ListAPIView):
    """Вывод списка квартир"""
    serializer_class = ApartmentDetailSerializer
    queryset = Apartment.objects.all()


class ApartmentDetailView(generics.RetrieveAPIView):
    """Просмотр квартиры"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer


class ApartmentCreateView(generics.CreateAPIView):
    """Добавление квартиры"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentCreateSerializer


class ApartmentUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование квартиры"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentCreateSerializer


class ApartmentDeleteView(generics.DestroyAPIView):
    """Удаление квартиры"""
    queryset = Apartment.objects.filter()
    serializer_class = ApartmentDetailSerializer


# --------------------------------------------------------------------------User


class AgentListView(generics.ListAPIView):
    """Вывод списка агентов"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_staff=True)


class ClientListView(generics.ListAPIView):
    """Вывод списка клиентов"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_staff=False)


class UserListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveAPIView):
    """Просмотр сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    """Добавление сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


# --------------------------------------------------------------------------Building


class BuildingListView(generics.ListAPIView):
    """Вывод списка зданий"""
    serializer_class = BuildingDetailSerializer
    queryset = Building.objects.all()


class BuildingDetailView(generics.RetrieveAPIView):
    """Просмотр здания"""
    queryset = Building.objects.all()
    serializer_class = BuildingDetailSerializer


class BuildingCreateView(generics.CreateAPIView):
    """Добавление здания"""
    queryset = Building.objects.all()
    serializer_class = BuildingCreateSerializer


class BuildingUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование здания"""
    queryset = Building.objects.all()
    serializer_class = BuildingCreateSerializer


class BuildingDeleteView(generics.DestroyAPIView):
    """Удаление здания"""
    queryset = Building.objects.filter()
    serializer_class = BuildingDetailSerializer


# --------------------------------------------------------------------------Contract


class ContractListView(generics.ListAPIView):
    """Вывод списка контрактов"""
    serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()


class ContractDetailView(generics.RetrieveAPIView):
    """Просмотр контракта"""
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer


class ContractCreateView(generics.CreateAPIView):
    """Добавление контракта"""
    queryset = Contract.objects.all()
    serializer_class = ContractCreateSerializer


class ContractUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование контракта"""
    queryset = Contract.objects.all()
    serializer_class = ContractCreateSerializer


class ContractDeleteView(generics.DestroyAPIView):
    """Удаление контракта"""
    queryset = Contract.objects.filter()
    serializer_class = ContractDetailSerializer
    #permission_class = permissions.IsAuthenticatedOrReadOnly
