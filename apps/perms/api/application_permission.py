# coding:utf-8
#


from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import Response

from common.permissions import IsOrgAdmin
from ..models import ApplicationPermission
from ..serializers import (
    ApplicationPermissionSerializer,
    ApplicationPermissionUpdateUserSerializer,
    ApplicationPermissionUpdateApplicationSerializer,
)


__all__ = [
    'ApplicationPermissionViewSet',
    'ApplicationPermissionAddUserApi',
    'ApplicationPermissionRemoveUserApi',
    'ApplicationPermissionAddApplicationApi',
    'ApplicationPermissionRemoveApplicationApi',
]


class ApplicationPermissionViewSet(viewsets.ModelViewSet):
    """
    应用授权列表的增删改查api
    """
    filter_fields = ['name']
    queryset = ApplicationPermission.objects.all()
    serializer_class = ApplicationPermissionSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsOrgAdmin,)


class ApplicationPermissionRemoveUserApi(RetrieveUpdateAPIView):
    """
    将用户从应用授权中移除，Detail页面会调用
    """
    permission_classes = (IsOrgAdmin,)
    serializer_class = ApplicationPermissionUpdateUserSerializer
    queryset = ApplicationPermission.objects.all()

    def update(self, request, *args, **kwargs):
        perm = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data.get('users')
            if users:
                perm.users.remove(*tuple(users))
            return Response({"msg": "ok"})
        else:
            return Response({"error": serializer.errors})


class ApplicationPermissionAddUserApi(RetrieveUpdateAPIView):
    permission_classes = (IsOrgAdmin,)
    serializer_class = ApplicationPermissionUpdateUserSerializer
    queryset = ApplicationPermission.objects.all()

    def update(self, request, *args, **kwargs):
        perm = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data.get('users')
            if users:
                perm.users.add(*tuple(users))
            return Response({"msg": "ok"})
        else:
            return Response({"error": serializer.errors})


class ApplicationPermissionRemoveApplicationApi(RetrieveUpdateAPIView):
    """
    将应用从授权中移除，Detail页面会调用
    """
    permission_classes = (IsOrgAdmin,)
    serializer_class = ApplicationPermissionUpdateApplicationSerializer
    queryset = ApplicationPermission.objects.all()

    def update(self, request, *args, **kwargs):
        perm = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            applications = serializer.validated_data.get('applications')
            if applications:
                perm.applications.remove(*tuple(applications))
            return Response({"msg": "ok"})
        else:
            return Response({"error": serializer.errors})


class ApplicationPermissionAddApplicationApi(RetrieveUpdateAPIView):
    permission_classes = (IsOrgAdmin,)
    serializer_class = ApplicationPermissionUpdateApplicationSerializer
    queryset = ApplicationPermission.objects.all()

    def update(self, request, *args, **kwargs):
        perm = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            applications = serializer.validated_data.get('applications')
            if applications:
                perm.applications.add(*tuple(applications))
            return Response({"msg": "ok"})
        else:
            return Response({"error": serializer.errors})
