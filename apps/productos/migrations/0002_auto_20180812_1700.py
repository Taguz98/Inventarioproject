# Generated by Django 2.1 on 2018-08-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
        ('local', '0002_stocklocal'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('codigo_producto', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='local.StockLocal')),
            ],
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_salida', models.CharField(default='Local Principal', max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('local_llegada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='local.Local')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('cedula', models.CharField(default='9999999999', max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='local.Local')),
            ],
        ),
        migrations.AddField(
            model_name='ingreso',
            name='descripcion',
            field=models.CharField(default='Prueba', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='local',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='local.Local'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='proveedor.Proveedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='id_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Ingreso'),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Producto'),
        ),
        migrations.AddField(
            model_name='detalleenvio',
            name='id_envio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Envio'),
        ),
        migrations.AddField(
            model_name='detalleenvio',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Producto'),
        ),
    ]
