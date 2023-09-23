from django.db import models
from core.models import BaseModel
from accounts.models import User
# Create your models here.


class Discount(BaseModel):
    percent = models.DecimalField(decimal_places=2)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

