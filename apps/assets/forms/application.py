# -*- coding: utf-8 -*-
#

from django import forms
from django.utils.translation import ugettext_lazy as _

from orgs.mixins import OrgModelForm

from ..models import Application, Asset, SystemUser
from .. import const

__all__ = [
    'ApplicationCreateUpdateForm',
]


class ApplicationTypeChromeForm(forms.ModelForm):
    chrome_target = forms.CharField(
        max_length=128, label=_('Target URL'), required=False
    )
    chrome_username = forms.CharField(
        max_length=128, label=_('Login username'), required=False
    )
    chrome_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Login password'), required=False
    )


class ApplicationTypeIEForm(forms.ModelForm):
    ie_target = forms.CharField(
        max_length=128, label=_('Target URL'), required=False
    )
    ie_username = forms.CharField(
        max_length=128, label=_('Login username'), required=False
    )
    ie_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Login password'), required=False
    )


class ApplicationTypePLSQLForm(forms.ModelForm):
    plsql_ip = forms.CharField(
        max_length=128, label=_('Database IP'), required=False
    )
    plsql_name = forms.CharField(
        max_length=128, label=_('Database name'), required=False
    )
    plsql_username = forms.CharField(
        max_length=128, label=_('Database username'), required=False
    )
    plsql_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Database password'), required=False
    )


class ApplicationTypeMSSQLForm(forms.ModelForm):
    mssql_ip = forms.CharField(
        max_length=128, label=_('Database IP'), required=False
    )
    mssql_name = forms.CharField(
        max_length=128, label=_('Database name'), required=False
    )
    mssql_username = forms.CharField(
        max_length=128, label=_('Database username'), required=False
    )
    mssql_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Database password'), required=False
    )


class ApplicationTypeMySQLWorkbenchForm(forms.ModelForm):
    mysql_workbench_ip = forms.CharField(
        max_length=128, label=_('Database IP'), required=False
    )
    mysql_workbench_name = forms.CharField(
        max_length=128, label=_('Database name'), required=False
    )
    mysql_workbench_username = forms.CharField(
        max_length=128, label=_('Database username'), required=False
    )
    mysql_workbench_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Database password'), required=False
    )


class ApplicationTypeVMwareForm(forms.ModelForm):
    vmware_target = forms.CharField(
        max_length=128, label=_('Target'), required=False
    )
    vmware_username = forms.CharField(
        max_length=128, label=_('Login username'), required=False
    )
    vmware_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Login password'), required=False
    )


class ApplicationTypeCustomForm(forms.ModelForm):
    custom_cmdline = forms.CharField(
        max_length=128, label=_('Operating parameter'), required=False
    )
    custom_target = forms.CharField(
        max_length=128, label=_('Target'), required=False
    )
    custom_username = forms.CharField(
        max_length=128, label=_('Login username'), required=False
    )
    custom_password = forms.CharField(
        widget=forms.PasswordInput, strip=True,
        max_length=128, label=_('Login password'), required=False
    )


class ApplicationTypeForms(
    ApplicationTypeChromeForm,
    ApplicationTypeIEForm,
    ApplicationTypePLSQLForm,
    ApplicationTypeMSSQLForm,
    ApplicationTypeMySQLWorkbenchForm,
    ApplicationTypeVMwareForm,
    ApplicationTypeCustomForm
):
    pass


class ApplicationCreateUpdateForm(ApplicationTypeForms, OrgModelForm):

    def __init__(self, *args, **kwargs):
        # 过滤RDP资产和系统用户
        super().__init__(*args, **kwargs)
        field_asset = self.fields['asset']
        field_asset.queryset = field_asset.queryset.filter(
            protocol=Asset.PROTOCOL_RDP
        )
        field_system_user = self.fields['system_user']
        field_system_user.queryset = field_system_user.queryset.filter(
            protocol=SystemUser.PROTOCOL_RDP
        )

    class Meta:
        model = Application
        fields = [
            'name', 'asset', 'system_user', 'type', 'path', 'comment'
        ]
        widgets = {
            'asset': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('Asset')
            }),
            'system_user': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('System user')
            })
        }

    def _get_params(self):
        app_type = self.data.get('type')
        fields = const.APP_TYPE_MAP_FIELDS.get(app_type, [])
        params = {}
        for field in fields:
            name = field['name']
            value = self.cleaned_data[name]
            params.update({name: value})
        return params

    def _save_params(self, instance):
        params = self._get_params()
        instance.params = params
        instance.save()
        return instance

    def save(self, commit=True):
        instance = super().save(commit=commit)
        instance = self._save_params(instance)
        return instance
