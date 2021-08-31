from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Official(models.Model):
    """Represents an official that can officiate games."""
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    level = models.IntegerField(
        help_text='The official\'s officiating level.',
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )

    def __str__(self):
        return '{} {} level {}'.format(
            self.first_name,
            self.last_name,
            self.level.__str__()
        )
