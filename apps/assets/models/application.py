# -*- coding: utf-8 -*-
#

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins import OrgModelMixin
from common.fields.model import JsonDictTextField
from common.utils import get_signer

from .. import const

signer = get_signer()

__all__ = [
    'Application',
]


class Application(OrgModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    asset = models.ForeignKey(
        'assets.Asset', on_delete=models.CASCADE, verbose_name=_('Asset')
    )
    system_user = models.ForeignKey(
        'assets.SystemUser', on_delete=models.CASCADE,
        verbose_name=_('System user')
    )
    type = models.CharField(
        default=const.APP_TYPE_CHROME, choices=const.APP_TYPE_CHOICES,
        max_length=128, verbose_name=_('Application type')
    )
    path = models.CharField(
        max_length=128, blank=False, null=False,
        verbose_name=_('Application path')
    )
    _params = JsonDictTextField(
        max_length=4096, blank=True, null=True, verbose_name=_('parameters')
    )
    created_by = models.CharField(
        max_length=32, null=True, blank=True, verbose_name=_('Created by')
    )
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_('Date created')
    )
    comment = models.TextField(
        max_length=128, default='', blank=True, verbose_name=_('Comment')
    )

    class Meta:
        unique_together = [('org_id', 'name')]
        verbose_name = _("Application")

    def __str__(self):
        return self.name

    @property
    def params(self):
        # 处理需要解密的字段
        _params = {}
        fields = const.APP_TYPE_MAP_FIELDS[self.type]
        for field in fields:
            name = field['name']
            encrypted = field['encrypted']
            value = self._params.get(name)
            if encrypted:
                value = signer.unsign(value)
            _params.update({name: value})

        return _params

    @params.setter
    def params(self, data):
        """
        :param data:
        {
            'chrome_app_path': '',
            'chrome_target': '',
            'chrome_username': '',
            'chrome_password': ''
        }
        """
        # 处理需要加密的字段
        _params = {}
        fields = const.APP_TYPE_MAP_FIELDS[self.type]
        for field in fields:
            name = field['name']
            encrypted = field['encrypted']
            value = data.get(name, '')
            if encrypted:
                value = signer.sign(value)
            _params.update({name: value})
        self._params = _params

    @property
    def asset_info(self):
        return {
            'id': self.asset.id,
            'hostname': self.asset.hostname
        }

    @property
    def system_user_info(self):
        return {
            'id': self.system_user.id,
            'name': self.system_user.name
        }
