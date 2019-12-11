
from django.urls import re_path
#distinguish users
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
        ])
    ),

})