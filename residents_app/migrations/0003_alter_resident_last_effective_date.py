# Generated by Django 5.0.7 on 2024-07-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents_app', '0002_delete_building_delete_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='last_effective_date',
            field=models.DateTimeField(),
        ),
    ]
