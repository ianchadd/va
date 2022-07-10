from django.conf.urls import url
from pt2.consumers import SliderPuzzleConsumer

websocket_routes = [
    url(r'^pt2/(?P<game_id>\w+)/$', SliderPuzzleConsumer),
]