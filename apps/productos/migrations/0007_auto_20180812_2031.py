# Generated by Django 2.1 on 2018-08-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20180812_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleingreso',
            name='codigo_producto',
            field=models.CharField(default='COD-000', max_length=8),
        ),
    ]