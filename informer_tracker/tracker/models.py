from __future__ import unicode_literals

from django.db import models

class Thana(models.Model):
	thanaId = models.CharField(max_length=200,blank=True)
	thanaName = models.CharField(max_length=400,blank=True)
	def __str__(self):
		return self.thanaName

class Chowki(models.Model):
	chowkiId = models.CharField(max_length=200,blank=True)
	chowkiName = models.CharField(max_length=400,blank=True)
	thana = models.ForeignKey(Thana, on_delete=models.CASCADE, blank=True)
	def __str__(self):
		return self.chowkiName


class Hulkas(models.Model):
	hulkasId = models.CharField(max_length=200,blank=True)
	hulkasName = models.CharField(max_length=400,blank=True)
	chowki = models.ForeignKey(Chowki, on_delete=models.CASCADE, blank=True)
	def __str__(self):
		return self.hulkasName


class Beats(models.Model):
	beatsId = models.CharField(max_length=200,blank=True)
	beatsName = models.CharField(max_length=400,blank=True)
	beatsPincode = models.IntegerField(default=0,blank=True)
	hulkas = models.ForeignKey(Hulkas, on_delete=models.CASCADE, blank=True)
	def __str__(self):
		return self.beatsName

class Informer(models.Model):
	name = models.CharField(max_length=200,blank=True)
	mobile = models.CharField(max_length=20,blank=True)
	pincode = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=400,blank=True)
	beats = models.ForeignKey(Beats, on_delete=models.CASCADE, blank=True)
