from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class IndexHomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_reserva"] = Reserva.objects.count()
        return context
    

class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi cadastrada com sucesso")
        return super().form_valid(form)

class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("lista_reservas")

    def form_valid(self, form):
        messages.warning(self.request, "Sua reserva foi cancelada")
        return super().form_valid(form)

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi atualizada com sucesso")
        return super().form_valid(form)


class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"  