# In the name of GOD

from django.db import models
from core.models import BaseModel
from order.models import Discount
import datetime.datetime as dt
from datetime import timedelta

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

