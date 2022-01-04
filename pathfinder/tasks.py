import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from allianceauth.notifications import notify
from celery import shared_task
from .models import PathfinderAccess
from allianceauth.services.tasks import QueueOnce
import requests

logger = logging.getLogger(__name__)

@shared_task(bind=True, name='pathfinder.update_members', base=QueueOnce)
def update_members(self):
    users = PathfinderAccess.objects.all().select_related('user').prefetch_related('user__character_ownerships') 
    id_list = []
    for user in users:
        for char in user.user.character_ownerships.all():
            id_list.append(char.character.character_id)
    id_list = ",".join(id_list)
    post_data = {'x-api-key': settings.PATHFINDER_API_KEY, 'character_ids':id_list}
    url = settings.PATHFINDER_URL + "api_write.php"
    r = requests.post(url, data=post_data)
    r.raise_for_status()
    return True


def user_has_account(self, user):
    try:
        user.pathfinder
    except ObjectDoesNotExist:
        return False
    else:
        return True
