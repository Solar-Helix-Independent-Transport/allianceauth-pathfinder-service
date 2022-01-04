import logging

from django.template.loader import render_to_string
from django.conf import settings

from allianceauth import hooks
from allianceauth.services.hooks import ServicesHook
from django.core.exceptions import ObjectDoesNotExist

from .tasks import update_members
from .urls import urlpatterns
from .models import PathfinderAccess

logger = logging.getLogger(__name__)


class PathfinderService(ServicesHook):
    def __init__(self):
        ServicesHook.__init__(self)
        self.urlpatterns = urlpatterns
        self.name = 'pathfinder'
        self.service_ctrl_template = 'services/pathfinder/pathfinder_service.html'
        self.access_perm = 'pathfinder.access_pathfinder'
        self.name_format = '{character_name}'

    def delete_user(self, user, notify_user=False):
        logger.debug('Deleting users %s %s account' % (user, self.name))
        PathfinderAccess.objects.filter(user=user).delete()
        update_members.apply_async(priority=7)
        return True

    def service_active_for_user(self, user):
        return user.has_perm(self.access_perm)

    def user_has_account(self, user):
        try:
            user.pathfinder
        except ObjectDoesNotExist:
            return False
        else:
            return True

    def render_services_ctrl(self, request):
        characters = request.user.character_ownerships.all().select_related('character')

        return render_to_string(self.service_ctrl_template, {
            'characters': characters if self.user_has_account(request.user) else {},
            'PATHFINDER_URL': getattr(settings, 'PATHFINDER_URL', ''),
            'PATHFINDER_NAME': getattr(settings, 'PATHFINDER_NAME', ''),
        }, request=request)


@hooks.register('services_hook')
def register_service():
    return PathfinderService()
