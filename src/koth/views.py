from django.shortcuts import render
from koth.models import Box, Player, Game, GamePlayer
from koth.serializers import BoxSerializer, PlayerSerializer, GameSerializer, GamePlayerSerializer
from rest_framework import viewsets, filters as bfilters
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters

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
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
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
