'''
Created on Feb 9, 2015

@author: Gilad
'''
from django.views.generic.base import View
from django.http.response import HttpResponse
import simplejson
from curling_club.apps.game_manager.models import Player, Game

class GetGames(View):
    
    def get(self, request, user, start_date, end_date):
        player = Player.objects.get(pk = user)
        games = player.get_games(start_date, end_date)
        return HttpResponse(simplejson.dumps(games), mimetype='application/json')
    
class ReportScore(View):
    
    def post(self, request, game, team, result):
        game_record = Game.objects.get(pk = game)
        result = game_record.record_result(team, result)
        return HttpResponse(simplejson.dumps(result), mimetype = 'application/json')
        