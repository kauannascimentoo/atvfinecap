from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission

class ReservaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi cadastrada")
        return super().form_valid(form)


class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"
    paginate_by = 2

class ReservaDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:lista_reservas")

    def form_valid(self, form):
        messages.error(self.request, "Sua reserva foi cancelada")
        return super().form_valid(form)
  
class ReservaUpdateView(GerentePermission, LoginRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi atualizada")
        return super().form_valid(form)

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"  