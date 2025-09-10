"""
ASGI config for flint_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns

# Set up the Django ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flint_project.settings')
django_asgi_app = get_asgi_application()

# Protocol type router for HTTP and WebSocket
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(websocket_urlpatterns),
})
