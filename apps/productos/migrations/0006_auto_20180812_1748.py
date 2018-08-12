# Generated by Django 2.1 on 2018-08-12 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20180812_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='id_venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='productos.Venta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='envio',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='descripcion',
            field=models.CharField(default='Descripcion del ingreso', max_length=200),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]