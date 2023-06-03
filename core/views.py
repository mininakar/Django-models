from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core import models, forms
from django.views.generic import ListView, DetailView
from core.models import Medicines, Сustomer, Suppliers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

def index (request):
    html = "<html> <body> Hi world! </body> </html>"
    return HttpResponse (html)
# Create your views here.


class MedList (ListView):
    model = Medicines
    template_name = 'core/med_list.html'
    def get_queryset(self):
        name = self.request.GET.get('name')
        #price = self.request.GET.get('price')
        qs = models.Medicines.objects.all()
        if name: #or price#
            return qs.filter (Q(name__icontains = name))
        return qs

    def __str__(self):
        return self.title

    def get_context_data(self):
        context = super().get_context_data()
        context ['form'] = forms.MedSearch(self.request.GET or None)
        context ['count'] = self.get_queryset().count()
        return context


class MedViews(DetailView):
    model = Medicines
    template_name = 'core/med_list.html'
    extra_context = {'title': f'Лекарство', 'flag': True}

class CustomerList (ListView):
    model = Сustomer
    template_name = 'core/customer_list.html'

class SuppliersList (ListView):
    model = Suppliers
    template_name = 'core/sup_list.html'

def detail_sup_view(request, sup_pk):
    suppliers = get_object_or_404(Suppliers, pk=sup_pk)
    context = {'title': f'Поставщик - {suppliers.name_supplier}',
               'flag': True,
               'suppliers': suppliers}

    return render(request, 'core/sup_list.html', context=context)


class MedCreate (TitleMixin, CreateView):
    model = models.Medicines
    template_name = 'core/med_create.html'
    form_class = forms.MedCreate
    success_url = reverse_lazy('core:med_list')
class MedUpdate (TitleMixin, UpdateView):
    model = models.Medicines
    template_name = 'core/med_create.html'
    form_class = forms.MedCreate
    success_url = reverse_lazy('core:med_list')

class MedDelete (TitleMixin, DeleteView):
    model = models.Medicines
    template_name = 'core/med_delete.html'
    success_url = reverse_lazy('core:med_list')
