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

class Product(BaseModel):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='products/images', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount,null=True, blank=True, on_delete=models.SET_NULL)
    # discount = models.ForeignKey(Discount, default=get_defualt_discount, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    
    @property
    def discounted_price(self):
        if self.discount:
            if self.discount.start_time <= dt.now() >= self.discount.end_time:
                return ((self.price)*(self.discount.percent))/100
        return 0
    @property
    def sell_price(self):
        return (self.price)-(self.discounted_price)
