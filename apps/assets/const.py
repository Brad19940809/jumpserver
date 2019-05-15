# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext_lazy as _


UPDATE_ASSETS_HARDWARE_TASKS = [
   {
       'name': "setup",
       'action': {
           'module': 'setup'
       }
   }
]

ADMIN_USER_CONN_CACHE_KEY = "ADMIN_USER_CONN_{}"
TEST_ADMIN_USER_CONN_TASKS = [
    {
        "name": "ping",
        "action": {
            "module": "ping",
        }
    }
]

ASSET_ADMIN_CONN_CACHE_KEY = "ASSET_ADMIN_USER_CONN_{}"

SYSTEM_USER_CONN_CACHE_KEY = "SYSTEM_USER_CONN_{}"
TEST_SYSTEM_USER_CONN_TASKS = [
   {
       "name": "ping",
       "action": {
           "module": "ping",
       }
   }
]


ASSET_USER_CONN_CACHE_KEY = 'ASSET_USER_CONN_{}_{}'
TEST_ASSET_USER_CONN_TASKS = [
    {
        "name": "ping",
        "action": {
            "module": "ping",
        }
    }
]


TASK_OPTIONS = {
    'timeout': 10,
    'forks': 10,
}

CACHE_KEY_ASSET_BULK_UPDATE_ID_PREFIX = '_KEY_ASSET_BULK_UPDATE_ID_{}'


# Application

APP_TYPE_CHROME = 'chrome'
APP_TYPE_MYSQL_WORKBENCH = 'mysql_workbench'
APP_TYPE_VMWARE = 'vmware'
APP_TYPE_CUSTOM = 'custom'

APP_TYPE_CHOICES = (
    (
        _('Browser'),
        (
            (APP_TYPE_CHROME, 'Chrome'),
        )
    ),
    (
        _('Database tools'),
        (
            (APP_TYPE_MYSQL_WORKBENCH, 'MySQL Workbench'),
        )
    ),
    (
        _('Virtualization tools'),
        (
            (APP_TYPE_VMWARE, 'VMware Client'),
        )
    ),
    (
        _('Custom'),
        (
            (APP_TYPE_CUSTOM, 'Custom'),
        )
    )

)

APP_TYPE_CHROME_FIELDS = [
    {'name': 'chrome_target', 'encrypted': False},
    {'name': 'chrome_username', 'encrypted': False},
    {'name': 'chrome_password', 'encrypted': True}
]
APP_TYPE_MYSQL_WORKBENCH_FIELDS = [
    {'name': 'mysql_workbench_ip', 'encrypted': False},
    {'name': 'mysql_workbench_name', 'encrypted': False},
    {'name': 'mysql_workbench_username', 'encrypted': False},
    {'name': 'mysql_workbench_password', 'encrypted': True}
]
APP_TYPE_VMWARE_FIELDS = [
    {'name': 'vmware_target', 'encrypted': False},
    {'name': 'vmware_username', 'encrypted': False},
    {'name': 'vmware_password', 'encrypted': True}
]
APP_TYPE_CUSTOM_FIELDS = [
    {'name': 'custom_cmdline', 'encrypted': False},
    {'name': 'custom_target', 'encrypted': False},
    {'name': 'custom_username', 'encrypted': False},
    {'name': 'custom_password', 'encrypted': True}
]

APP_TYPE_MAP_FIELDS = {
    APP_TYPE_CHROME: APP_TYPE_CHROME_FIELDS,
    APP_TYPE_MYSQL_WORKBENCH: APP_TYPE_MYSQL_WORKBENCH_FIELDS,
    APP_TYPE_VMWARE: APP_TYPE_VMWARE_FIELDS,
    APP_TYPE_CUSTOM: APP_TYPE_CUSTOM_FIELDS
}
