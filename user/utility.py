from django.contrib import auth
from rest_framework.authtoken.models import Token
import datetime
import jwt
from django.conf import settings

def create_token(username, password):
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        return token
    return None


def generate_access_token(user):

    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              "settings.SECRET_KEY", algorithm='HS256')
    return access_token
