import base64
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User

__author__ = 'ktisha'

class CustomUserBackend(RemoteUserBackend):
    create_unknown_user = False

    def authenticate(self, remote_user):
        print(remote_user)
        auth = remote_user.split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).decode("utf-8").split(':')
                user = User.objects.get(username=uname)
                return user
        return super().authenticate(remote_user)
