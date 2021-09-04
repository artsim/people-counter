from django.urls import path

from counter import consumers

websocket_urlpatterns = [
    path("ws/polldata/", consumers.DataConsumer.as_asgi()),
]
