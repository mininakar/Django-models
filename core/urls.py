from django.urls import path, include
from core import views
from .views import *

app_name = 'core'
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('med_list/', views.MedList.as_view(), name ='med_list'),
    path('sup_list/', views.SuppliersList.as_view(), name="sup_list"),
    path('sup/<int:sup_pk>/', detail_sup_view, name="sup"),
    path('med_create/', views.MedCreate.as_view(), name ='med_create'),
    path('med_update/<int:pk>', views.MedUpdate.as_view(), name ='med_update'),
    path('med_delete/<int:pk>', views.MedDelete.as_view(), name ='med_delete'),
]