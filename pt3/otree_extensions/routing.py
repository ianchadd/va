from django.conf.urls import url
from pt3.consumers import SliderPuzzleConsumer

websocket_routes = [
    url(r'^pt3/(?P<game_id>\w+)/$', SliderPuzzleConsumer),
]