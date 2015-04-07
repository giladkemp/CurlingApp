'''
Created on Feb 9, 2015

@author: Gilad
'''
from curling_club.apps.game_manager.views import GetGames, ReportScore
from django.conf.urls import patterns

urlpatterns = patterns('',
                       (r'^games/', GetGames.as_view()),
                       (r'^report/', ReportScore.as_view()),
                )