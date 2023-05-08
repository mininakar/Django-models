from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core import models
from django.views.generic import ListView, DetailView
from core.models import Medicines, Сustomer, Suppliers



def index (request):
    html = "<html> <body> Hi world! </body> </html>"
    return HttpResponse (html)
# Create your views here.


class MedList (ListView):
    model = Medicines
    template_name = 'core/med_list.html'

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
