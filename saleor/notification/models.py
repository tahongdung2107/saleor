from django.db import models
from ..core.permissions import NotificationPermissions


class Notification(models.Model):
    name = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ("pk",)
        permissions = ((NotificationPermissions.MANAGE_NOTIFICATIONS.codename,
                        "Manage notification."),)

    def __str__(self):
        return self.name
