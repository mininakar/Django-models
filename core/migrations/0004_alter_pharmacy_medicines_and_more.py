# Generated by Django 4.2.1 on 2023-05-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_pharmacyid_pharmacy_medicines_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='medicines',
            field=models.ManyToManyField(blank=True, null=True, related_name='medicines_as_pharmacy', to='core.medicines'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_manager',
            field=models.CharField(max_length=100, verbose_name='Фармацевт'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_name',
            field=models.CharField(max_length=50, verbose_name='Название аптеки'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='name_supplier',
            field=models.CharField(max_length=50, verbose_name='Название поставщика'),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='requisites_sup',
            field=models.IntegerField(blank=True, null=True, verbose_name='Реквизиты'),
        ),
        migrations.AlterField(
            model_name='сustomer',
            name='name_customer',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='сustomer',
            name='requisites_cust',
            field=models.IntegerField(blank=True, null=True, verbose_name='Реквизиты'),
        ),
    ]