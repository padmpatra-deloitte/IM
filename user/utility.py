from django.contrib import auth
from rest_framework.authtoken.models import Token

def create_token(username, password):
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        print("Before token " + token)
        token, _ = Token.objects.get_or_create(user=user)
        print("after token " + token)
        return token
    return None