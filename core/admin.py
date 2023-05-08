from django.contrib import admin
from core import models
# Register your models here.

admin.site.register(models.Medicines)
admin.site.register (models.Pharmacy)
admin.site.register (models.Сustomer)
admin.site.register (models.Suppliers)
class Medicines (admin.ModelAdmin):
    list_display = ()

class Pharmacy (admin.ModelAdmin):
    list_display = ()

class Сustomer (admin.ModelAdmin):
    list_display =()