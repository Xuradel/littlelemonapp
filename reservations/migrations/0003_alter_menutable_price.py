# Generated by Django 4.2.5 on 2023-09-10 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_bookingtable_menutable_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutable',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]