# coding: utf-8
#

from django import forms
from orgs.mixins import OrgModelForm
from django.utils.translation import ugettext_lazy as _

from ..models import ApplicationPermission

__all__ = [
    'ApplicationPermissionCreateUpdateForm',
]


class ApplicationPermissionCreateUpdateForm(OrgModelForm):
    class Meta:
        model = ApplicationPermission
        exclude = (
            'id', 'date_created', 'created_by', 'org_id'
        )
        widgets = {
            'users': forms.SelectMultiple(
                attrs={'class': 'select2', 'data-placeholder': _("User")}
            ),
            'user_groups': forms.SelectMultiple(
                attrs={'class': 'select2', 'data-placeholder': _("User group")}
            ),
            'applications': forms.SelectMultiple(
                attrs={'class': 'select2', 'data-placeholder': _("Application")}
            )
        }

    def clean_user_groups(self):
        users = self.cleaned_data.get('users')
        user_groups = self.cleaned_data.get('user_groups')

        if not users and not user_groups:
            raise forms.ValidationError(
                _("User or group at least one required"))
        return self.cleaned_data["user_groups"]
