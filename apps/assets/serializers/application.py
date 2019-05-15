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
        fields = [
            'id', 'name', 'asset', 'system_user', 'type', 'path', 'comment',
            'created_by', 'date_created',  'params',
            'asset_info', 'system_user_info', 'get_type_display', 'org_id',
        ]
        read_only_fields = (
            'created_by', 'date_created', 'asset_info', 'system_user_info',
            'get_type_display', 'org_id'
        )

    def _save_params(self, instance):
        instance.params = self.validated_data.get('params', {})
        instance.save()
        return instance

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        instance = self._save_params(instance)
        return instance

