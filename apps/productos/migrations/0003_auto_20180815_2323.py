# Generated by Django 2.1 on 2018-08-16 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Stock'),
        ),
    ]