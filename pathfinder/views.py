import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from .models import PathfinderAccess
from .tasks import update_members

logger = logging.getLogger(__name__)

ACCESS_PERM = 'pathfinder.access_pathfinder'

@login_required
@permission_required(ACCESS_PERM)
def deactivate_pathfinder(request):
    PathfinderAccess.objects.filter(user=request.user).delete()
    update_members.apply_async(priority=3)
    return redirect("services:services")


@login_required
@permission_required(ACCESS_PERM)
def activate_pathfinder(request):
    pathfinder_user = PathfinderAccess()
    pathfinder_user.user = request.user
    pathfinder_user.save()
    update_members.apply_async(priority=3)
    return redirect("services:services")

