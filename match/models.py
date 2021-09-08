from django.db import models

from league.models import Day
from officials.models import Official
from participant.models import Participant
from team.models import Team


class TeamGame(models.Model):
    """Represents a team's involvement in a match. Holds team specific information about the match."""
    GAME_STATUS = (
        ('scheduled', 'Scheduled'),
        ('played', 'Played'),
        ('default', 'Default'),
        ('forfeit', 'Forfeit'),
    )

    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)

    score = models.IntegerField(
        help_text='The team\'s score for the game.'
    )
    status = models.CharField(
        max_length=255,
        choices=GAME_STATUS
    )

    def get_match(self):
        """Returns the match of this team game, might be home or away, so we check both!"""
        try:
            return self.match_home_team
        except Match.DoesNotExist:
            try:
                return self.match_away_team
            except Match.DoesNotExist:
                return ''

    def __str__(self):
        return '{} playing {}'.format(
            self.team.__str__(),
            self.get_match().__str__()
        )

    def add_participant(self, participant_pk, participant_number=000):
        """Add a participant to this Team Game"""
        if participant_pk is None:
            return False
        try:
            participant = Participant.objects.get(pk=participant_pk)
        except Participant.DoesNotExist:
            return False

        player = Player(participant=participant, game=self, number=participant_number)
        player.save()

        return True


class Match(models.Model):
    """Represents a match to be played by two teams and officiated by officials."""
    day = models.ForeignKey(to=Day, on_delete=models.CASCADE, related_name='matches')
    time = models.TimeField(
        help_text='Date and time when this match is happening.'
    )
    home_team = models.OneToOneField(
        to=TeamGame,
        on_delete=models.CASCADE,
        related_name='match_home_team'
    )
    away_team = models.OneToOneField(
        to=TeamGame,
        on_delete=models.CASCADE,
        related_name='match_away_team'
    )

    def __str__(self):
        return '{} vs {}'.format(
            self.home_team.team.__str__(),
            self.away_team.team.__str__(),
        )


class OfficialGame(models.Model):
    """Represents an official's involvement in a match"""
    OFFICIAL_STATUS = (
        ('scheduled', 'Scheduled'),
        ('attended', 'Attended'),
        ('missed', 'Missed')
    )
    status = models.CharField(
        max_length=255,
        choices=OFFICIAL_STATUS,
    )
    match = models.ForeignKey(
        to=Match,
        on_delete=models.CASCADE,
        related_name='officials'
    )
    official = models.ForeignKey(
        to=Official,
        on_delete=models.CASCADE,
        related_name='games'
    )

    def __str__(self):
        return '{} officiating {}'.format(
            self.official.__str__(),
            self.match.__str__()
        )


class Player(models.Model):
    """Represents a participant's involvement on a game."""
    participant = models.ForeignKey(
        to=Participant,
        on_delete=models.CASCADE,
        related_name='player_set'
    )
    game = models.ForeignKey(
        to=TeamGame,
        on_delete=models.CASCADE,
        related_name='players'
    )

    number = models.PositiveIntegerField(
        help_text='The player\'s game jersey number.',
        null=True,
        blank=True,
    )
    score = models.PositiveIntegerField(
        help_text='The amount of points the player scored.',
        default=0
    )
    fouls = models.PositiveIntegerField(
        help_text='The amount of fouls the player committed.',
        default=0
    )
    is_mvp = models.BooleanField(
        default=False,
        help_text='Is the player the game\'s MVP?'
    )

    def __str__(self):
        return '{} playing {}'.format(
            self.participant.__str__(),
            self.game.__str__()
        )
