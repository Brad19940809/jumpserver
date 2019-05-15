# -*- coding: utf-8 -*-
#

from rest_framework import serializers
from ..models import ApplicationPermission


__all__ = [
    'ApplicationPermissionSerializer',
    'ApplicationPermissionUpdateUserSerializer',
    'ApplicationPermissionUpdateApplicationSerializer',
]


class ApplicationPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationPermission
        fields = [
            'id', 'name', 'users', 'user_groups', 'applications', 'comment',
            'is_active', 'date_start', 'date_expired', 'is_valid',
            'created_by', 'date_created', 'org_id'
        ]
        read_only_fields = ['created_by', 'date_created', 'is_valid']


class ApplicationPermissionUpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationPermission
        fields = ['id', 'users']


class ApplicationPermissionUpdateApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationPermission
        fields = ['id', 'applications']
