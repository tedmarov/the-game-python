from django.db import models
from django.db.models.fields.related import ForeignKey
from rest_framework.authtoken.models import Token

class Event(models.Model):
    host=models.ForeignKey(Token, on_delete=models.CASCADE)