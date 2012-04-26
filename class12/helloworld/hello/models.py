from django.db import models

# Create your models here.
class Todo(models.model):
	name = models.CharField(max_length=200)
	finished = models.BooleanField()