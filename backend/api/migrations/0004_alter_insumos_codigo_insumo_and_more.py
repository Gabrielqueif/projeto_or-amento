# Generated by Django 5.1.7 on 2025-03-17 02:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_codigo_insumo_id_remove_insumos_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumos',
            name='codigo_insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.codigo_insumo', unique=True),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='coodigo_insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.codigo_insumo', unique=True),
        ),
    ]
