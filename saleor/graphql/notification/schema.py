import graphene

from .mutations.notification import (
    NotificationCreate,
    NotificationUpdate,
    NotificationDelete,
)

from ...notification import models
from .types import (
    NotificationType
)


class NotificationQueries(graphene.ObjectType):
    all_notification = graphene.List(NotificationType)

    def resolve_all_notification(self, info, **kwargs):
        return models.Notification.objects.all()


class NotificationMutations(graphene.ObjectType):
    notification_create = NotificationCreate.Field()
    notification_update = NotificationUpdate.Field()
    notification_delete = NotificationDelete.Field()
