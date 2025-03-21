# Generated by Django 5.1.7 on 2025-03-18 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_insumos_codigo_insumo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insumos",
            name="codigo_insumo",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="api.codigo_insumo",
            ),
        ),
        migrations.AlterField(
            model_name="tabela",
            name="coodigo_insumo",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="api.codigo_insumo",
            ),
        ),
    ]
