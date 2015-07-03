# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('symbol', models.CharField(max_length=10)),
                ('buy_ss', models.CharField(max_length=2, choices=[(b'B', b'Buy'), (b'S', b'Sell'), (b'SC', b'Short Cover'), (b'SS', b'Short Sell')])),
                ('quantity', models.DecimalField(max_digits=19, decimal_places=0)),
                ('price', models.DecimalField(max_digits=19, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=10)),
                ('buy_ss', models.CharField(max_length=2, choices=[(b'B', b'Buy'), (b'S', b'Sell'), (b'SC', b'Short Cover'), (b'SS', b'Short Sell')])),
                ('quantity', models.DecimalField(max_digits=19, decimal_places=0)),
                ('value', models.DecimalField(max_digits=19, decimal_places=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('user_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('cash_bal', models.DecimalField(default=Decimal('100000'), max_digits=19, decimal_places=2)),
                ('net_worth', models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('margin', models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2)),
                ('no_trans', models.DecimalField(default=Decimal('0'), max_digits=19, decimal_places=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_data',
            fields=[
                ('symbol', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('current_price', models.DecimalField(max_digits=19, decimal_places=2)),
                ('high', models.DecimalField(max_digits=19, decimal_places=2)),
                ('low', models.DecimalField(max_digits=19, decimal_places=2)),
                ('open_price', models.DecimalField(max_digits=19, decimal_places=2)),
                ('change', models.DecimalField(max_digits=19, decimal_places=2)),
                ('change_per', models.DecimalField(max_digits=19, decimal_places=2)),
                ('trade_Qty', models.DecimalField(max_digits=19, decimal_places=2)),
                ('trade_Value', models.DecimalField(max_digits=19, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=10)),
                ('buy_ss', models.CharField(max_length=2, choices=[(b'B', b'Buy'), (b'SS', b'Short Sell')])),
                ('quantity', models.DecimalField(max_digits=19, decimal_places=0)),
                ('value', models.DecimalField(max_digits=19, decimal_places=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
