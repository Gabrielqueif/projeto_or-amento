# Generated by Django 5.1.7 on 2025-03-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_insumos_codigo_insumo_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="estados",
            name="id",
        ),
        migrations.AlterField(
            model_name="estados",
            name="sigla",
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
