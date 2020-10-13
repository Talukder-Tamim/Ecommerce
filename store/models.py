from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.CharField(max_length=200, default='', blank=True, null=False)
	image = models.ImageField(upload_to='uploads/products/')

	def __str__(self):
		return self.name


