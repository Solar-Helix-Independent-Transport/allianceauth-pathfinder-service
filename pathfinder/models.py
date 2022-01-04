from django.contrib.auth.models import User
from django.db import models


class PathfinderAccess(models.Model):
    user = models.OneToOneField(User,
                                primary_key=True,
                                on_delete=models.CASCADE,
                                related_name='pathfinder')

    def __str__(self):
        return "Pathfinder - {}".format(self.user.username)

    class Meta:
        permissions = (
            ("access_pathfinder", u"Can access Pathfinder on any linked character"),
        )
