from django.db import models
from django.db.models import Model
#Предметная область: Деканат (успеваемость студентов).



class Medicines (Model):
    name = models.CharField('Название препарата', max_length= 100, blank=False)
    date_issue = models.DateField('Дата выпуска', help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    expiry_date = models.DateField("Срок годности", help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    price = models.FloatField("Цена", default=0)

    def __str__(self):
        return self.name


class Suppliers (Model):
    name_supplier = models.CharField("Название поставщика", max_length= 50, blank=False)
    requisites_sup =  models.IntegerField ("Реквизиты", blank=True,null=True)
    medicines = models.ForeignKey(Medicines, on_delete=models.CASCADE,blank=True, null=True )
    def __str__(self):
        return self.name_supplier
class Pharmacy(Model):
    pharmacy_name =  models.CharField("Название аптеки",max_length= 50, blank=False)
    pharmacy_manager = models.CharField ("Фармацевт",max_length= 100, blank=False)
    phone = models.IntegerField ("Номер",blank=True,null=True)
    medicines = models.ManyToManyField(Medicines, blank=True,  related_name="medicines_as_pharmacy")
    def __str__(self):
        return self.pharmacy_name


class Сustomer (Model):
    name_customer = models.CharField("ФИО", max_length=255, blank=False)
    requisites_cust = models.IntegerField("Реквизиты",blank=True,null=True)
    pharmacy = models.ManyToManyField(Pharmacy, blank=True)
    def __str__(self):
        return self.name_customer
