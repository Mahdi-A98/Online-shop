# In the name of GOD
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from core.manager import BaseManager
# Create your models here.

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True,
        verbose_name=_("Datetime of deletion"),
        help_text=_("This is deleted datetime"))

    is_deleted = models.BooleanField(default=False,
            verbose_name=_("Deleted status"),
            help_text=_("This is deleted status"))

    is_active = models.BooleanField(default=True,
            verbose_name=_("Acive status"),
            help_text=_("This is active status"))
    
    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(Self):
        self.is_active = True
        self.save()