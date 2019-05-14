# -*- coding: utf-8 -*-
#


from rest_framework import serializers
from common.mixins import BulkSerializerMixin
from common.serializers import AdaptedBulkListSerializer
from common.fields.serializer import DictField

from ..models import Application


__all__ = [
    'ApplicationSerializer',
]


class ApplicationSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    params = DictField()

    class Meta:
        model = Application
        list_serializer_class = AdaptedBulkListSerializer
        fields = '__all__'

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.extend([
            'asset_info', 'system_user_info', 'get_type_display'
        ])
        return fields
