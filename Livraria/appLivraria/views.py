from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from appLivraria.models import Empresa
from django.urls.base import reverse_lazy
from .forms import EmpresaForm


class index(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'index.html'


class EmpresaListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastraEmp.html'
    model = Empresa


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "cadastraEmp.html"
    model = Empresa()
    form_class = EmpresaForm
    success_url = reverse_lazy("cadastraEmp")
    fields = '__all__'


class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm


def questionario(request):
    form = EmpresaForm()
    return render(request, 'formulario.html', {'form': form})
