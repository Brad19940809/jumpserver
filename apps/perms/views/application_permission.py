# coding:utf-8
#

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DetailView, ListView
)
from django.views.generic.edit import SingleObjectMixin
from django.conf import settings

from common.permissions import AdminUserRequiredMixin
from orgs.utils import current_org
from users.models import UserGroup
from assets.models import Application

from ..models import ApplicationPermission
from ..forms import ApplicationPermissionCreateUpdateForm


__all__ = [
    'ApplicationPermissionListView', 'ApplicationPermissionCreateView',
    'ApplicationPermissionUpdateView', 'ApplicationPermissionDetailView',
    'ApplicationPermissionUserView', 'ApplicationPermissionApplicationView',
]


class ApplicationPermissionListView(AdminUserRequiredMixin, TemplateView):
    template_name = 'perms/application_permission_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Perms'),
            'action': _('Application permission list'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationPermissionCreateView(AdminUserRequiredMixin, CreateView):
    model = ApplicationPermission
    form_class = ApplicationPermissionCreateUpdateForm
    template_name = 'perms/application_permission_create_update.html'
    success_url = reverse_lazy('perms:application-permission-list')

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Perms'),
            'action': _('Create application permission'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationPermissionUpdateView(AdminUserRequiredMixin, UpdateView):
    model = ApplicationPermission
    form_class = ApplicationPermissionCreateUpdateForm
    template_name = 'perms/application_permission_create_update.html'
    success_url = reverse_lazy("perms:application-permission-list")

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Perms'),
            'action': _('Update application permission')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationPermissionDetailView(AdminUserRequiredMixin, DetailView):
    model = ApplicationPermission
    form_class = ApplicationPermissionCreateUpdateForm
    template_name = 'perms/application_permission_detail.html'
    success_url = reverse_lazy("perms:application-permission-list")

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Perms'),
            'action': _('Update application permission'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationPermissionUserView(AdminUserRequiredMixin,
                                    SingleObjectMixin,
                                    ListView):
    template_name = 'perms/application_permission_user.html'
    context_object_name = 'application_permission'
    paginate_by = settings.DISPLAY_PER_PAGE
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=ApplicationPermission.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = list(self.object.get_all_users())
        return queryset

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Perms'),
            'action': _('Application permission user list'),
            'users_remain': current_org.get_org_users().exclude(
                application_permissions=self.object
            ),
            'user_groups_remain': UserGroup.objects.exclude(
                application_permissions=self.object
            )
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationPermissionApplicationView(AdminUserRequiredMixin,
                                           SingleObjectMixin,
                                           ListView):
    template_name = 'perms/application_permission_application.html'
    context_object_name = 'application_permission'
    paginate_by = settings.DISPLAY_PER_PAGE
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=ApplicationPermission.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = list(self.object.get_all_applications())
        return queryset

    def get_context_data(self, **kwargs):
        applications_granted = self.get_queryset()
        print("g: ", applications_granted)
        applications_remain = Application.objects.exclude(id__in=[a.id for a in applications_granted])
        print('r: ', applications_remain)
        context = {
            'app': _('Perms'),
            'action': _('Asset permission asset list'),
            'applications_remain': applications_remain
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
