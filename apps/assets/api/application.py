# -*- coding: utf-8 -*-
#

from rest_framework_bulk import BulkModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from ..models import Application
from .. import serializers

from ..hands import IsOrgAdmin

__all__ = [
    'ApplicationViewSet'
]


class ApplicationViewSet(BulkModelViewSet):
    filter_fields = ("name",)
    search_fields = filter_fields
    permission_classes = (IsOrgAdmin,)
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    pagination_class = LimitOffsetPagination
