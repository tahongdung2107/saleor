import graphene
from ...core.mutations import ModelMutation, ModelDeleteMutation
from ....notification import models
from ..types import (
    NotificationInput,
    NotificationType
)
from ...core.types.common import NotificationError
from ....core.permissions import NotificationPermissions


class NotificationCreate(ModelMutation):
    class Arguments:
        input = NotificationInput(
            required=True, description="Fields required to create notification."
        )

    class Meta:
        description = "Create a new notification."
        model = models.Notification
        return_field_name = "notification"
        error_type_class = NotificationError
        error_type_field = "notification_errors"

    @classmethod
    def save(cls, info, instance, cleaned_input):
        models.Notification(
            name=cleaned_input['name'],
            content=cleaned_input['content'],
            active=cleaned_input['active']
        ).save()


class NotificationUpdate(NotificationCreate):
    notification = graphene.Field(NotificationType,
                                  description="An updated notification.")

    class Arguments:
        id = graphene.ID(required=True, description="ID of a notification to update.")
        input = NotificationInput(
            required=True, description="Fields required to update a notification."
        )

    class Meta:
        description = "Updates a notification."
        # permissions = (NotificationPermissions.MANAGE_NOTIFICATIONS,)
        model = models.Notification
        error_type_class = NotificationError
        error_type_field = "notification_errors"

    @classmethod
    def perform_mutation(cls, root, info, **data):
        instance = models.Notification.objects.get(pk=data['id'])
        if instance:
            instance.content = data['input'].content
            instance.name = data['input'].name
            instance.active = data['input'].active
            instance.save()
            return NotificationUpdate(notification=instance)
        return NotificationUpdate(notification=None)


class NotificationDelete(ModelDeleteMutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of a notification to delete.")

    class Meta:
        description = "delete a notification."
        model = models.Notification
        error_type_class = NotificationError
        error_type_field = "notification_errors"

    @classmethod
    def perform_mutation(cls, root, info, **data):
        instance = models.Notification.objects.get(pk=data['id'])
        if instance:
            instance.delete()
            return cls.success_response(instance)
        return cls.success_response(instance)

