from rest_framework_json_api import serializers
from koth.models import Box, Player, Game, GamePlayer

class BoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Box
        fields = ('os', 'title', 'flags')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('level', 'avatar', 'username', 'country')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('box', 'started_at', 'finished_at', 'first_hacked', 'status', 'game_type', 'king_found', 'king_changes', 'resets', 'creator_name')

class GamePlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GamePlayer
        fields = ('game', 'player', 'score', 'flags', 'rank', 'king')

