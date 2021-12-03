import graphene
from ...notification import models
from ..core.connection import CountableDjangoObjectType
from graphene import relay


class NotificationInput(graphene.InputObjectType):
    name = graphene.String(description="name notification", required=True)
    content = graphene.String(description="content notification", required=True)
    active = graphene.Boolean(description="active notification", required=True)


class NotificationType(CountableDjangoObjectType):
    name = graphene.String(description="Given name")
    content = graphene.String(description="Given content")
    active = graphene.Boolean(description="Given active")

    class Meta:
        description = "Represents notification data."
        interfaces = [relay.Node]
        model = models.Notification
        only_fields = [
            "name",
            "content",
            "active",
        ]
