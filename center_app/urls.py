from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


app_name = "center_app"

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('apartments/', ApartmentListView.as_view()),
    path('apartment/<int:pk>/', ApartmentDetailView.as_view()),
    path('apartment/create/', ApartmentCreateView.as_view()),
    path('apartment/update/<int:pk>/', ApartmentUpdateView.as_view()),
    path('apartment/delete/<int:pk>/', ApartmentDeleteView.as_view()),

    path('users/', UserListView.as_view()),
    path('agents/', AgentListView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/update/<int:pk>/', UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', UserDeleteView.as_view()),


    path('buildings/', BuildingListView.as_view()),
    path('building/<int:pk>/', BuildingDetailView.as_view()),
    path('building/create/', BuildingCreateView.as_view()),
    path('building/update/<int:pk>/', BuildingUpdateView.as_view()),
    path('building/delete/<int:pk>/', BuildingDeleteView.as_view()),

    path('contracts/', ContractListView.as_view()),
    path('contract/<int:pk>/', ContractDetailView.as_view()),
    path('contract/create/', ContractCreateView.as_view()),
    path('contract/update/<int:pk>/', ContractUpdateView.as_view()),
    path('contract/delete/<int:pk>/', ContractDeleteView.as_view()),
]
