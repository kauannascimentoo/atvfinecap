from django.shortcuts import render, get_object_or_404, redirect
from reservas.models import Reserva
from stands.models import Stand
from django.views import generic
# Create your views here.


class IndexHomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_reserva"] = Reserva.objects.count()
        context["total_stands"] = Stand.objects.count()
        return context