from django.db import models
class User(models.Model):
	user_id=models.CharField(max_length=200,primary_key=True)
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	def _str_(self):
		return self.user_id
		
