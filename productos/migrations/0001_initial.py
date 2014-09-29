# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoCantidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('producto', models.OneToOneField(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoPrecio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(max_digits=19, decimal_places=2)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('producto', models.OneToOneField(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
