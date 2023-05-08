from django.shortcuts import render
from core.models import Medicines


def index (request):
    all_med = Medicines.objects.all()
    print(all_med)
# Create your views here.
