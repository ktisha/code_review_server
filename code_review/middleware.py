__author__ = 'ktisha'
from django.contrib.auth.middleware import RemoteUserMiddleware


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_AUTHORIZATION'