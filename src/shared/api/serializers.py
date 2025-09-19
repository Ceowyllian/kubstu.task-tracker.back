from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import (
    ModelSerializer,
)
from rest_framework.serializers import Serializer as EmptySerializer

from . import fields

__all__ = [
    "ReadOnlyMixin",
    "DataObjectSerializer",
    "EmptySerializer",
]


class ReadOnlyMixin:
    def save(self, **kwargs):
        self.__fail()

    def create(self, validated_data):
        self.__fail()

    def update(self, instance, validated_data):
        self.__fail()

    def __fail(self):
        error_message = (
            "`%s` serializer is supposed to be read-only." % self.__class__.__name__
        )
        raise TypeError(error_message)  # pragma: no cover


class DataObjectSerializer(
    ModelSerializer,
    ReadOnlyMixin,
):
    id = fields.UUIDField(
        read_only=True,
        help_text=_("Object ID"),
    )
    created = fields.DateTimeField(
        read_only=True,
        help_text=_("Creation date and time"),
    )
    modified = fields.DateTimeField(
        read_only=True,
        help_text=_("Modification date and time"),
    )

    class Meta:
        abstract = True
        fields = [
            "id",
            "created",
            "modified",
        ]
