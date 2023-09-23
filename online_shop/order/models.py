from django.db import models
from core.models import BaseModel
from accounts.models import User
# Create your models here.


class Discount(BaseModel):
    percent = models.DecimalField(decimal_places=2)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

class Order(BaseModel):
    payment_status = [("U", "Unpaid"), ("P", "Paid")]
    status_choices = [('P', 'Processing'), ('A', 'Approved'), ('C', 'Canceled')]
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True, editable=False)
    status = models.CharField(verbose_name=_("Order Status"), max_length=1, choices=status_choices, default="P")
    payment = models.CharField(verbose_name=_("Payment Status"), max_length=1, choices=payment_status, default="U")
    customer = model.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=set.null)

    class Meta:
        permissions =[
            ('change_order_status', 'can change order approval status' ),
            ('change_payment_status', 'can change order Payment status' ),
        ]

    @property
    def get_order_items(self):
        order_items = order_item.objects.filter(order=self.id)
        return order_items

    @property
    def total_price(self):
        order_itemorder_item = self.get_order_items
        order_total_price = 0
        for item in order_itemorder_item:
            order_total_price += item.total_price
        return order_total_price

    def __str__(self):
        return f"Order{self.id}"
