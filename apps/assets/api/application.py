# -*- coding: utf-8 -*-
#

from rest_framework import generics
from rest_framework_bulk import BulkModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .. import serializers
from ..models import Application
from ..hands import IsOrgAdmin, IsAppUser, IsOrgAdminOrAppUser

__all__ = [
    'ApplicationViewSet', 'ApplicationConnectionInfoApi',
]


class ApplicationViewSet(BulkModelViewSet):
    filter_fields = ("name",)
    search_fields = filter_fields
    permission_classes = (IsOrgAdmin,)
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    pagination_class = LimitOffsetPagination


class ApplicationConnectionInfoApi(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    # permission_classes = (IsAppUser,)
    permission_classes = (IsOrgAdminOrAppUser,)
    serializer_class = serializers.ApplicationConnectionInfoSerializer
