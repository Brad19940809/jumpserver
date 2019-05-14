# coding:utf-8
#

from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from common.permissions import AdminUserRequiredMixin
from common.const import create_success_msg, update_success_msg
from ..models import Application
from .. import forms

__all__ = [
    'ApplicationListView', 'ApplicationCreateView', 'ApplicationUpdateView',
    'ApplicationDetailView'
]


class ApplicationListView(AdminUserRequiredMixin, TemplateView):
    template_name = 'assets/application_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Application list'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class ApplicationCreateView(AdminUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Application
    form_class = forms.ApplicationCreateUpdateForm
    template_name = 'assets/application_create_update.html'
    success_url = reverse_lazy('assets:application-list')

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Create application'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return create_success_msg % ({'name': cleaned_data['name']})


class ApplicationUpdateView(AdminUserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Application
    form_class = forms.ApplicationCreateUpdateForm
    template_name = 'assets/application_create_update.html'
    success_url = reverse_lazy('assets:application-list')

    def get_initial(self):
        return {k: v for k, v in self.object.params.items()}

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Update application'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return update_success_msg % ({'name': cleaned_data['name']})


class ApplicationDetailView(AdminUserRequiredMixin, DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'assets/application_detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Application detail'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)