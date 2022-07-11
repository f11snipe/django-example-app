from django.shortcuts import render
from django.db.models import Avg, Max, Count, Sum
from koth.models import Box, Player, Game, GamePlayer
from koth.serializers import BoxSerializer, PlayerSerializer, PlayerDetailSerializer, GameSerializer, GamePlayerSerializer
from rest_framework import viewsets, filters as bfilters
from rest_framework_json_api import filters, django_filters

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    filter_backends = (filters.QueryParameterValidationFilter, filters.OrderingFilter,
                        django_filters.DjangoFilterBackend, bfilters.SearchFilter)
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'os': ('icontains', 'iexact', 'contains'),
        'title': ('icontains', 'iexact', 'contains')
    }
    search_fields = ('id', 'os', 'title',)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.annotate(
        num_games=Count('gameplayer'),
        avg_rank=Avg('gameplayer__rank'),
        avg_score=Avg('gameplayer__score'),
        total_score=Sum('gameplayer__score'),
        avg_king=Avg('gameplayer__king'),
        total_king=Sum('gameplayer__king'),
        avg_flags=Avg('gameplayer__flags'),
        total_flags=Sum('gameplayer__flags'),
    ).all()
    serializer_class = PlayerDetailSerializer
    filter_backends = (filters.QueryParameterValidationFilter, filters.OrderingFilter,
                        django_filters.DjangoFilterBackend, bfilters.SearchFilter)
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'level': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'username': ('icontains', 'iexact', 'contains')
    }
    search_fields = ('id', 'level', 'username',)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GamePlayerViewSet(viewsets.ModelViewSet):
    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer
