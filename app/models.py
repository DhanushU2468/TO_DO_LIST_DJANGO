from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
class CompleteTask(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
class Trash(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
# Create your models here.
