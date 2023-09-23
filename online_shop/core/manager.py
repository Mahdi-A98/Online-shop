from django.db import models


class BaseManager(models.Manager):

    def get_queryset(self):
        """
        same as get_queryset but fitering logical deleted items
        """
        return super().get_queryset().filter(is_deleted=False)

    def get_deleted_list(self):
        """
        define deleted item for easy access data
        """
        return super().get_queryset(is_deleted=True)

    def get_archive(self):
        """
        define method for access all queryset
        """
        return super().get_queryset()

    def get_active_list(self):
        """
        define method for access all active query
        """
        return self.get_queryset.filter(is_active=True)

    def get_deacitive_list(self):
        """
        define deactivate item
        """
        return self.get_queryset(is_active=False)
