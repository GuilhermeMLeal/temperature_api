
from .models import UserEntity
import jwt
from django.conf import settings
from datetime import datetime, timedelta


def authenticate(username, password):
    # regra de autenticação
    if username == 'user' and password == 'a1b2c3': 
        # deveria retornar os dados encontrados no banco
        return UserEntity(username=username)
    return None

def generateToken(user):
    payload = {
        'username' : user.username,
        'exp' : datetime.utcnow() + timedelta(minutes=10) 
    }
    return jwt.encode(payload = payload, 
                      key = getattr(settings, 'SECRET_KEY'),
                      algorithm = 'HS256')

def refreshToken(user):
    return generateToken(user)

def verifyToken(token):
    error_code = 0

    try: 
        payload = jwt.decode(jwt = token, 
                      key = getattr(settings, 'SECRET_KEY'),
                      algorithms = ['HS256'])
    except jwt.ExpiredSignatureError:
        error_code = 1
    except jwt.InvalidTokenError:
        error_code = 2

    return [error_code, payload]

def getAuthenticatedUser(token):
    _, payload = verifyToken(token)

    if payload is not None:
        return UserEntity(username=payload['username'])
