from django.db import models


class Participant(models.Model):
    """Represents a user that can participate in one or many teams"""
    PARTICIPANT_STATUS = (
        ('can_play', 'Can Play'),
        ('suspended', 'Suspended'),
    )

    ubc_uuid = models.CharField(
        max_length=255,
        help_text='The user\'s PUID from ubc.'
    )
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    ubc_id = models.CharField(
        max_length=255,
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    signed_waiver = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=PARTICIPANT_STATUS)

    def __str__(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )
