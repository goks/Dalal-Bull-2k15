from __future__ import absolute_import

from celery import shared_task
from dalalbull.celery import app

from login.models import Stock_data 
import urllib2
import json
import datetime

#TODO:insert operation must be done// 52 imports??is it necessary??
#db initialisation insert the comany details initially
#urllib2 performance constraints and exception handling??
@app.task
def Update_db():
    now = datetime.datetime.now()
    if(now.strftime("%A")!='Sunday'):
		start_time=datetime.time(hour=10,minute=00,second=00)
		end_time=datetime.time(hour=17,minute=00,second=00)
		now = datetime.datetime.now().strftime('%H:%M:%S')
		if(start_time<now<end_time):
			response=urllib2.urlopen('http://nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json')
			json_data=json.load(response)
			for company in json_data['data']:
				c=Stock_data.objects.get(symbol=company['symbol'])
				c.current_price=company['ltP']
				c.high=company['high']
				c.low=company['low']
				c.open_price=company['open']
				c.change=company['ptsC']
				c.change_per=company['per']
				c.trade_Qty=company['trdVol']
				c.trade_value=company['ntP']
	    		c.save()
			company=json_data['latestData']
			c=Stock_data.objects.get(symbol='NIFTY')
			c.current_price=company['ltp']
			c.high=company['high']
			c.low=company['low']
			c.open_price=company['open']
			c.change=company['ch']
			c.change_per=company['per']
			c.trade_Qty=json_data['trdVolumesum']
			c.trade_value=json_data['trdValuesum']
			c.save()
           
