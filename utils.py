from aiohttp import ClientSession
import datetime
from jose import jwt


async def request(url, mode="json"):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            return await getattr(resp, mode)()


def create_token(data: dict):
    from .main import settings
    access_token = jwt.encode({
        'userInfo': data,
        'iat': datetime.datetime.now(),
        'iss': settings.JWT.get('iss'),
        'exp': datetime.datetime.now() + settings.JWT.get('access_exp')
    }, settings.SECRET, algorithm='HS512')

    refresh_token = jwt.encode({
        'iat': datetime.datetime.now(),
        'iss': settings.JWT.get('iss'),
        'exp': datetime.datetime.now() + settings.JWT.get('refresh_exp')
    }, settings.SECRET, algorithm='HS512')

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
