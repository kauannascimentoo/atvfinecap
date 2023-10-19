from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from .forms import StandForm
from .models import Stand
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission

# Create your views here.

class StandCreateView(GerentePermission, LoginRequiredMixin, generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Seu stand foi cadastrado")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class StandListView(LoginRequiredMixin, generic.ListView):
    model = Stand
    template_name = "lista_stands.html"
    paginate_by = 2

class StandUpdateView(GerentePermission, LoginRequiredMixin, generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Seu stand foi atualizado")
        return super().form_valid(form)

class StandDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stands:lista_stands")
    
    def form_valid(self, form):
        messages.error(self.request, "Seu stand foi removido")
        return super().form_valid(form)

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand
    template_name = "stand_detalhe.html" 