
from django.contrib import admin
from django.urls import path
from stands.views import StandCreateView, StandDeleteView, StandListView, StandUpdateView, StandDetailView

app_name = "stands"

urlpatterns = [
    path('lista_stands/', StandListView.as_view(), name='lista_stands'),
    path('reserva_stand/', StandCreateView.as_view(), name="reserva_stand"),
    path('remover_stand/<int:pk>/', StandDeleteView.as_view(), name="remover_stand"),
    path('update_stand/<int:pk>/', StandUpdateView.as_view(), name="editar_stand"),
    path('stand_detalhe/<int:pk>/', StandDetailView.as_view(), name='stand_detalhe'),
]

