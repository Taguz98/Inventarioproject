# Generated by Django 2.1 on 2018-08-15 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0005_auto_20180813_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklocal',
            name='ubicacion',
            field=models.CharField(max_length=50, verbose_name='Ubicacion producto'),
        ),
    ]