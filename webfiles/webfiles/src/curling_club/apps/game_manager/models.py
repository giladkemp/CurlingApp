'''
Created on Feb 2, 2015

@author: Gilad
'''
import datetime
from django.db import models
from django.db.models.fields.related import ManyToOneRel

class League(models.Model):
    name = models.CharField()
    coord_email = models.EmailField()
    rules = models.CharField()

class Player(models.Model):
    name = models.CharField()
    email = models.CharField()
    
    def get_games(self, start_date, end_date):
        teams = Team.objects.filter(models.Q(first = self) 
                                | models.Q(second = self) 
                                | models.Q(third = self) 
                                | models.Q(fourth = self))
        games = Game.objects.filter(models.Q(team1_contained_by = teams)
                                | models.Q(team2_contained_by = teams)).filter(time_gte = start_date).filter(time_lte = end_date)
        return games
    
class Team(models.Model):
    name = models.CharField()
    league = models.ManyToOneRel(League)
    first = models.ManyToOneRel(Player)
    second = models.ManyToOneRel(Player)
    third = models.ManyToOneRel(Player)
    fourth = models.ManyToOneRel(Player)
    
class Game(models.Model):
    team1 = ManyToOneRel(Team)
    team2 = ManyToOneRel(Team)
    time = models.DateTimeField()
    team1_report_date = models.DateTimeField()
    team2_report_date = models.DateTimeField()
    result = models.IntegerField()
    
    def record_result(self, team, result):
        if team:
            if self.team1_report_date is None:
                self.result = result
                self.team1_report_date = datetime.datetime.now()
                self.save()
                return 0 #Success
            return 1 #Team1 already reported a score for this game
        else:
            if self.team2_report_date is None:
                self.result = result
                self.team2_report_date = datetime.datetime.now()
                self.save()
                return 0; #Success
            return 2 #Team2 already reported a score for this game 
    