#The 52 tables corresponding to each of the companies must be made dynamically during first execution
# Company = type('Company', (models.Model,), {
#    'update_time': models.DateTimeField(auto_now_add),
#    'current_price': models.DecimalField(max_digits=19, decimal_places=2)})
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
class User(models.Model):
	user_id=models.CharField(max_length=200,primary_key=True)
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	def _str_(self):
		return self.user_id

class Portfolio(models.Model):
	user_id=models.CharField(max_length=200,primary_key=True)
	cash_bal=models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('100000'))
	net_worth=models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'),validators=[MinValueValidator(Decimal('0.00'))])
	margin=models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'))
	no_trans=models.DecimalField(max_digits=19, decimal_places=0, default=Decimal('0'))
	def _str_(self):
		return self.user_id

class Transaction(models.Model):
	user_id=models.CharField(max_length=200)
	symbol=models.CharField(max_length=10)
	PURCHASE_OPTIONS = (
        ('B', 'Buy'),
        ('SS', 'Short Sell')
    )
	buy_ss = models.CharField(max_length=2, choices=PURCHASE_OPTIONS)
	quantity=models.DecimalField(max_digits=19, decimal_places=0)
	value=models.DecimalField(max_digits=19,decimal_places=2)
	time=models.DateTimeField(auto_now_add=True)

class Pending(models.Model):
	user_id=models.CharField(max_length=200)
	symbol=models.CharField(max_length=10)
	PURCHASE_OPTIONS = (
        ('B', 'Buy'),
        ('S','Sell'),
        ('SC','Short Cover'),
        ('SS', 'Short Sell')
    )
	buy_ss = models.CharField(max_length=2, choices=PURCHASE_OPTIONS)
	quantity=models.DecimalField(max_digits=19, decimal_places=0)
	value=models.DecimalField(max_digits=19,decimal_places=2)
	time=models.DateTimeField(auto_now_add=True)

class history(models.Model):
	user_id=models.CharField(max_length=200)
	time=models.DateTimeField(auto_now_add=True)
	symbol=models.CharField(max_length=10)
	PURCHASE_OPTIONS = (
        ('B', 'Buy'),
        ('S','Sell'),
        ('SC','Short Cover'),
        ('SS', 'Short Sell')
    )
	buy_ss=models.CharField(max_length=2, choices=PURCHASE_OPTIONS)
	quantity=models.DecimalField(max_digits=19, decimal_places=0)
	price=models.DecimalField(max_digits=19,decimal_places=2)

class Stock_data(models.Model):
    symbol=models.CharField(max_length=10,primary_key=True)
    current_price=models.DecimalField(max_digits=19, decimal_places=2)
    high=models.DecimalField(max_digits=19, decimal_places=2)
    low=models.DecimalField(max_digits=19, decimal_places=2)
    open_price=models.DecimalField(max_digits=19, decimal_places=2)
    change=models.DecimalField(max_digits=19, decimal_places=2)
    change_per=models.DecimalField(max_digits=19, decimal_places=2)
    trade_Qty=models.DecimalField(max_digits=19, decimal_places=2)
    trade_Value=models.DecimalField(max_digits=19, decimal_places=2)
