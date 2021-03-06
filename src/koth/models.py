import datetime
from tkinter import CASCADE

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Box(models.Model):
    # TODO: ENUM
    os = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    flags = models.IntegerField('number of possible flags')
    def __str__(self):
        return self.title


class Player(models.Model):
    level = models.IntegerField(default=0)
    avatar = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    # TODO: ENUM?
    country = models.CharField(max_length=3)
    # TODO: Methods/fields for metrics
    # player.gameplayer_set.count() -- Total games played
    #  users = Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'))
    # Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'), total_king=Sum('gameplayer__king'), avg_king=Avg('gameplayer__king'))
    def __str__(self):
        return self.username

class Game(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    # thmid = models.IntegerField('thm game id')
    started_at = models.DateTimeField('start time')
    finished_at = models.DateTimeField('finish time', null=True)
    first_hacked = models.DateTimeField('first hacked time', null=True)
    # TODO: ENUM
    status = models.CharField(max_length=64)
    # TODO: ENUM
    game_type = models.CharField(max_length=64)
    king_found = models.BooleanField(default=False)
    king_changes = models.IntegerField(default=0)
    resets = models.IntegerField(default=0)
    creator_name = models.CharField(max_length=255, default='unknown')
    players = models.ManyToManyField(Player, through='GamePlayer')
    # creator = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='creator')
    # winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner')
    # chartData = ??
    # tableData = ??
    # userIds = [ xxx, yyy, zzz ]
    def was_played_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.started_at <= now
    def __str__(self):
        return f"Game #{self.id}"


class GamePlayer(models.Model):
    game = models.ForeignKey(Game, related_name='gameplayers', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    flags = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    king = models.IntegerField(default=0)
