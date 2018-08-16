# Generated by Django 2.1 on 2018-08-16 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0002_stocklocal_producto'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('ubicacion', models.CharField(default='Sin ubicacion', max_length=100)),
                ('local_envio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='envio_llegada', to='local.Local')),
                ('local_llegada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='local.Local')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='local.StockLocal')),
            ],
        ),
    ]