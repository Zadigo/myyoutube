from django.urls import re_path
from videos.consumers import FeedBuilderConsumer

websocket_urlpatterns = [
    re_path(
        r'^ws/feed-builder$',
        FeedBuilderConsumer.as_asgi()
    )
]
