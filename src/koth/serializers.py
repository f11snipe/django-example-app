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

class PlayerDetailSerializer(serializers.HyperlinkedModelSerializer):
    num_games = serializers.IntegerField()
    avg_rank = serializers.FloatField()
    avg_score = serializers.FloatField()
    total_score = serializers.IntegerField()
    avg_king = serializers.FloatField()
    total_king = serializers.IntegerField()
    avg_flags = serializers.FloatField()
    total_flags = serializers.IntegerField()
    class Meta:
        model = Player
        fields = ('level', 'avatar', 'username', 'country', 'num_games', 'avg_rank', 'avg_score', 'total_score', 'avg_king', 'total_king', 'avg_flags', 'total_flags')

class GamePlayerSerializer(serializers.HyperlinkedModelSerializer):
    player = PlayerSerializer(many=False, read_only=True)

    class Meta:
        model = GamePlayer
        # depth = 1
        fields = ('game', 'player', 'score', 'flags', 'rank', 'king')



class GameSerializer(serializers.HyperlinkedModelSerializer):
    gameplayers = GamePlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        depth = 1
        fields = ('box', 'gameplayers', 'started_at', 'finished_at', 'first_hacked', 'status', 'game_type', 'king_found', 'king_changes', 'resets', 'creator_name')
