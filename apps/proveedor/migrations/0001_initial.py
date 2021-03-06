# Generated by Django 2.1 on 2018-08-20 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuentasProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50, verbose_name='Banco/Cooperativa')),
                ('tipo_cuenta', models.CharField(choices=[('AHORRO', 'Ahorro'), ('CORRIENTE', 'Corriente')], max_length=12)),
                ('numero_cuenta', models.CharField(max_length=15, verbose_name='Numero cuenta')),
            ],
            options={
                'ordering': ['proveedor'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40, verbose_name='Direccion/Ciudad')),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(blank=True, max_length=40, null=True)),
                ('ruc', models.CharField(max_length=13)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='cuentasproveedor',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.Proveedor'),
        ),
    ]
