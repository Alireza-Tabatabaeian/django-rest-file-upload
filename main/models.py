from django.contrib.auth.models import User
from django.db import models


class Category(models.IntegerChoices):
    Literature = 1
    Biography = 2
    Science = 3
    Physic = 4
    Math = 5


class EditRequest(models.Model):
    doc = models.FileField(upload_to='docs')
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    category = models.IntegerField(choices=Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
