from django.shortcuts import render
from django.db.models import Avg, Max, Count, Sum
from koth.models import Box, Player, Game, GamePlayer
from koth.serializers import BoxSerializer, PlayerSerializer, PlayerDetailSerializer, GameSerializer, GamePlayerSerializer
from django_filters import rest_framework as rfilters
from rest_framework import viewsets, filters as bfilters
from rest_framework_json_api import filters, django_filters

class GameFilter(rfilters.FilterSet):
    min_king_changes = rfilters.NumberFilter(field_name="king_changes", lookup_expr='gte')
    max_king_changes = rfilters.NumberFilter(field_name="king_changes", lookup_expr='lte')
    class Meta:
        model = Game
        # fields = ['status', 'game_type', 'king_found', 'creator_name',  'box__os', 'box__title']
        fields = {
            'box__os': ['exact', 'iexact', 'icontains'],
            'box__title': ['exact', 'iexact', 'icontains'],
            'players__country': ['exact', 'iexact'],
            'players__username': ['exact', 'iexact'],
            'status': ['exact', 'iexact'],
            'game_type': ['exact', 'iexact'],
            'started_at': ['lte', 'gte'],
            'king_found': ['exact'],
            'king_changes': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'resets': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    filter_backends = (filters.QueryParameterValidationFilter, filters.OrderingFilter,
                        django_filters.DjangoFilterBackend, bfilters.SearchFilter)
    # filterset_fields = {
    #     'os': ('icontains', 'iexact', 'contains'),
    #     'title': ('icontains', 'iexact', 'contains')
    # }
    filterset_fields = ['os', 'title']
    search_fields = ('os', 'title',)

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
    # filterset_fields = {
    #     'level': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
    #     'username': ('icontains', 'iexact', 'contains')
    # }
    filterset_fields = ['level', 'username', 'country']
    search_fields = ('username')

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = (filters.QueryParameterValidationFilter, filters.OrderingFilter,
                        django_filters.DjangoFilterBackend, bfilters.SearchFilter,)
    filterset_class = GameFilter
    # filterset_fields = ['status', 'game_type', 'king_found', 'king_changes', 'resets', 'creator_name', 'started_at', 'finished_at']
    search_fields = ('creator_name', 'box__os', 'box__title')

class GamePlayerViewSet(viewsets.ModelViewSet):
    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer
