from django.conf.urls import include
from django.urls import re_path

from . import views

app_name = 'pathfinder'

module_urls = [
    # Discord Service Control
    re_path(r'^activate/$', views.activate_pathfinder, name='activate'),
    re_path(r'^deactivate/$', views.deactivate_pathfinder, name='deactivate'),
]

urlpatterns = [
    re_path(r'^pathfinder/', include((module_urls, app_name), namespace=app_name))
]
