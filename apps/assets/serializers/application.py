# -*- coding: utf-8 -*-
#


from rest_framework import serializers
from common.mixins import BulkSerializerMixin
from common.serializers import AdaptedBulkListSerializer
from common.fields.serializer import DictField

from ..models import Application
from .. import const


__all__ = [
    'ApplicationSerializer', 'ApplicationConnectionInfoSerializer',
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


class ApplicationConnectionInfoSerializer(serializers.ModelSerializer):
    remote_app_params = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = [
            'id', 'name', 'asset', 'system_user', 'remote_app_params',
        ]

    @staticmethod
    def get_remote_app_params(obj):
        parameters = [obj.type]
        path = '\"{}\"'.format(obj.path)
        parameters.append(path)
        fields = const.APP_TYPE_MAP_FIELDS[obj.type]
        for field in fields:
            value = obj.params.get(field['name'])
            parameters.append(value)

        params = {
            'program': '||boot-program-name',
            'working_directory': '',
            'parameters': " ".join(parameters)
        }
        return params
