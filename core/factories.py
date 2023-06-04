import factory
from faker import Factory

from core import models
factory_ru = Factory.create ("ru-Ru")

class Medicines (factory.django.DjangoModelFactory):
    name = factory_ru.word()
    date_issue = factory_ru.date()
    expiry_date = factory_ru.date()
    price = factory_ru.random_number()

    class Meta:
        model = models.Medicines