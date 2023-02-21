from django.conf.urls import url
from pt3.consumers import SliderPuzzleConsumer

websocket_routes = [
    url(r'^pt1_VA/(?P<game_id>\w+)/$', SliderPuzzleConsumer),
]