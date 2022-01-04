from django.conf.urls import url, include

from . import views

app_name = 'pathfinder'

module_urls = [
    # Discord Service Control
    url(r'^activate/$', views.activate_pathfinder, name='activate'),
    url(r'^deactivate/$', views.deactivate_pathfinder, name='deactivate'),
]

urlpatterns = [
    url(r'^pathfinder/', include((module_urls, app_name), namespace=app_name))
]
