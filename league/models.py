import datetime

from django.db import models
from multiselectfield import MultiSelectField


class Gender(models.Model):
    """Represents a gender that can be used in Pools."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tier(models.Model):
    """Represents a tier that can be used in Pools."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Term(models.Model):
    """Represents a term that can be used in Pools."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    """Represents a location where a game can be played."""
    name = models.CharField(
        max_length=255,
        help_text='Use an easy to read name of the location.'
    )

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Represents an actual league activity"""
    name = models.CharField(
        max_length=255,
        help_text='The name of the activity, use a descriptive name users can understand!'
    )

    def __str__(self):
        return self.name


class Pool(models.Model):
    """Represents a pool for an activity."""
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )

    name = models.CharField(
        max_length=255,
        help_text='The pool name, use something descriptive.'
    )
    game_duration = models.DurationField(
        help_text='The time duration of each game played in this pool.',
        default=datetime.timedelta(minutes=60)
    )
    days_of_play = MultiSelectField(
        choices=DAY_CHOICES,
        min_choices=1,
        help_text='What days is this pool playing?'
    )

    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)

    gender = models.ForeignKey(to=Gender, on_delete=models.CASCADE)
    tier = models.ForeignKey(to=Tier, on_delete=models.CASCADE)
    term = models.ForeignKey(to=Term, on_delete=models.CASCADE)
    locations_of_play = models.ManyToManyField(to=Location)

    def __str__(self):
        return '{} {}'.format(self.activity.name, self.name)


class Week(models.Model):
    """Represents a week of play where days can be filled with games."""
    start_date = models.DateField(
        help_text='The first day of the week.'
    )
    end_date = models.DateField(
        help_text='The last day of the week.'
    )

    pool = models.ForeignKey(to=Pool, on_delete=models.CASCADE)

    def __str__(self):
        return 'Week of {} to {}.'.format(self.start_date.day, self.end_date.day)


class Day(models.Model):
    """Represents a day of play within a week. The day can have any number of games scheduled."""
    week = models.ForeignKey(to=Week, on_delete=models.CASCADE)

    day = models.DateField()
    start_time = models.TimeField(help_text='Time when the first game can start!')
    end_time = models.TimeField(help_text='Last hour a game can be played this day. (Not the last start time)')
    location = models.ForeignKey(
        to=Location,
        help_text='Location where this day\'s games are to be played.',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} day of play for {} at {}'.format(
            self.week.pool.__str__(), self.day.__str__(), self.location.__str__()
        )
