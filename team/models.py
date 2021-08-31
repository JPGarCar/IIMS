from django.db import models

from league.models import Pool
from participant.models import Participant


class Unit(models.Model):
    """Represents a Unit a Team can be a part of"""
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    """Represents a Team that can play in an activity Pool"""
    name = models.CharField(
        max_length=255,
    )
    team_number = models.IntegerField()
    pool = models.ForeignKey(
        to=Pool,
        on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        to=Unit,
        on_delete=models.CASCADE
    )
    secondary_unit = models.ForeignKey(
        to=Unit,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='secondary_unit'
    )

    team_roster = models.ManyToManyField(
        to=Participant,
        related_name='team_roster',
    )
    team_captain = models.ForeignKey(
        to=Participant,
        on_delete=models.CASCADE,
        related_name='team_captain'
    )

    def __str__(self):
        return '{}'.format(
            self.name
        )
