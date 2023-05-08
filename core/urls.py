from django.urls import path, include
from core import views
from .views import *

app_name = 'core'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('med_list/', views.MedList.as_view(), name ='med_list'),
    path('sup_list/', views.SuppliersList.as_view(), name="sup_list"),
    path('sup/<int:sup_pk>/', detail_sup_view, name="sup"),
]