# Generated by Django 4.2.1 on 2023-05-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pharmacyid_alter_medicines_date_issue_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PharmacyId',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='medicines',
            field=models.ManyToManyField(blank=True, null=True, to='core.medicines'),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='medicines',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.medicines'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='pharmacy',
            field=models.ManyToManyField(blank=True, to='core.pharmacy'),
        ),
    ]
