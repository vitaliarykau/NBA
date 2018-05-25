from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

MIN_SCORES = 50
MAX_SCORES = 170
MATCHES_IN_SEASON = 82
MAX_POINTS = 150
MAX_STAT = 50
MAX_NUMBER_ON_JERSEY = 99
MAX_WEIGHT = 200


class Position(models.Model):
    position = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.position


class College(models.Model):
    name = models.CharField(max_length=30, verbose_name='College name',
                            unique=True)

    def __str__(self):
        return self.name


class Nationality(models.Model):
    country = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'nationalities'
    def __str__(self):
        return self.country


class Conference(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    season = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s/%s" % (self.season, self.season + 1)


class Arena(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    establish = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Coach(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    b_day = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.surname)

    class Meta:
        verbose_name_plural = 'Coaches'


class Team(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=3)
    city = models.CharField(max_length=30)
    coach = models.OneToOneField(Coach, on_delete=models.PROTECT, unique=True)
    arena = models.ForeignKey(Arena, on_delete=models.PROTECT)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)
    logo = models.ImageField('Logo', upload_to='teams_logo', default='', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s %s" %(self.city, self.name)


class Player(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    b_day = models.DateField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField(blank=True, null=True,
                                              validators = [MaxValueValidator(MAX_WEIGHT)])
    number = models.PositiveSmallIntegerField(validators = [MaxValueValidator(MAX_NUMBER_ON_JERSEY)])
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    college = models.ForeignKey(College, blank=True, null=True, on_delete=models.PROTECT)
    image = models.ImageField('Photo', upload_to='players_profiles', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s %s" %(self.name, self.surname)

    class Meta:
        ordering = ['surname']


class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team, verbose_name='Home Team', on_delete=models.PROTECT, related_name='team1')
    score1 = models.PositiveSmallIntegerField(verbose_name='Home Scores',
                                              validators = [MinValueValidator(MIN_SCORES),
                                                            MaxValueValidator(MAX_SCORES)])
    team2 = models.ForeignKey(Team, verbose_name='Away Team',on_delete=models.SET_NULL, null=True,
                              related_name='team2')
    score2 = models.PositiveSmallIntegerField(verbose_name='Away Scores',
                                              validators = [MinValueValidator(MIN_SCORES),
                                                            MaxValueValidator(MAX_SCORES)])
    arena = models.ForeignKey(Arena, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'matches'
        permissions = (
            ('statistic.can_moderate', 'Moderate data in app statistic'),
        )

    def __str__(self):
        return '{} {} {}:{} {}'.format(self.date, self.team1.short_name.upper(),
                                       self.score1, self.score2, self.team2.short_name.upper())

    def clean(self):
        if self.date > timezone.localdate():
            raise ValidationError('Date must be from the past!')
        try:
            if self.team1 == self.team2:
                raise ValidationError('Only different teams can play match!')
        except:
            raise ValidationError('Add both teams!')

        if self.score1 == self.score2:
            raise ValidationError('There are no matches with draw in NBA')
        try:
            self.arena
        except:
            raise ValidationError('Add a venue!')

        this_day = Match.objects.filter(date=self.date)
        if this_day.exists():
            for match in this_day:
                if match.team1 == self.team1:
                    raise ValidationError(("Team %s has already played this day") % self.team1)
                elif match.team2 == self.team1:
                    raise ValidationError(("Team %s has already played this day") % self.team1)
                if match.team1 == self.team2:
                    raise ValidationError(("Team %s has already played this day") % self.team2)
                elif match.team2 == self.team2:
                    raise ValidationError(("Team %s has already played this day") % self.team2)


class Stat(models.Model):
        season = models.ForeignKey(Season, on_delete=models.PROTECT)
        player = models.ForeignKey(Player, on_delete=models.PROTECT)
        team = models.ForeignKey(Team, on_delete=models.PROTECT)
        number_matches = models.PositiveSmallIntegerField(default=0,
                                                          validators = [MaxValueValidator(MATCHES_IN_SEASON)])
        time = models.TimeField(default='00:00')
        points = models.FloatField(default=0, validators = [MaxValueValidator(MAX_POINTS)])
        rebounds = models.FloatField(default=0, validators = [MaxValueValidator(MAX_STAT)])
        assists = models.FloatField(default=0, validators=[MaxValueValidator(MAX_STAT)])
        steals = models.FloatField(default=0, validators=[MaxValueValidator(MAX_STAT)])
        blocks = models.FloatField(default=0, validators = [MaxValueValidator(MAX_STAT)])

        def __str__(self):
            return '%s in %s' % (self.player, self.season)

        class Meta:
            permissions = (
                ('statistic.can_moderate', 'Moderate data in app statistic'),
            )
