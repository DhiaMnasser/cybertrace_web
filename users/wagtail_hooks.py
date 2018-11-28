from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf.urls import url, include

from wagtail.core import hooks
from .views import RulesView
from . import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [url(r'^members/', include(urls, namespace='users'))]

@hooks.register('register_admin_menu_item')
def add_another_welcome_panel():
    return MenuItem(
        'Rules',
        reverse('users:rules_view'),
        classnames='icon icon-form',
        order=1000
    )
