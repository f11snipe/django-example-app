# django-example-app
Example app using python + django framework

### Metrics ideas

```
>>> users = Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'))
>>> users = Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'))
>>> users = Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'), total_king=Sum('gameplayer__king'))
>>> users = Player.objects.filter(username='F11snipe').annotate(num_games=Count('gameplayer'), total_king=Sum('gameplayer__king'), avg_king=Avg('gameplayer__king'))
>>> top_users = Player.objects.annotate(total_king=Sum('gameplayer__king')).order_by('-total_king')[:5]
>>> top_users = Player.objects.annotate(avg_king=Avg('gameplayer__king')).order_by('-avg_king')[:5]
>>> flags = Player.objects.annotate(avg_flags=Avg('gameplayer__flags')).order_by('-avg_flags')[:5]
>>> flags = Player.objects.annotate(num_flags=Sum('gameplayer__flags')).order_by('-num_flags')[:5]
>>> ranks = Player.objects.annotate(avg_rank=Avg('gameplayer__rank')).order_by('-avg_rank')[:5]
>>> ranks = Player.objects.annotate(avg_rank=Avg('gameplayer__rank')).order_by('-level', '-avg_rank')[:5]
>>> ranks = Player.objects.annotate(avg_rank=Avg('gameplayer__rank')).order_by('+avg_rank')[:5]
>>> ranks = Player.objects.annotate(avg_rank=Avg('gameplayer__rank')).order_by('avg_rank')[:5]
>>> snipe = Player.objects.annotate(avg_rank=Avg('gameplayer__rank')).filter(username='F11snipe')[0]
>>> scores = Player.objects.annotate(avg_score=Avg('gameplayer__score')).order_by('-avg_score')[:5]
>>> scores = Player.objects.annotate(num_games=Count('gameplayer'), avg_score=Avg('gameplayer__score')).filter(num_games__gt=2).order_by('-avg_score')[:5]
>>> scores = Player.objects.annotate(num_games=Count('gameplayer'), avg_score=Avg('gameplayer__score')).filter(num_games__gt=10).order_by('-avg_score')[:5]
>>> scores = Player.objects.annotate(total_score=Sum('gameplayer__score')).order_by('-total_score')[:5]
```
