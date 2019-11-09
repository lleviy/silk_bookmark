"""В этом файле собраны все необходимые настройки для api подключения к сторонним сайтам"""

from unsplash.api import Api
from unsplash.auth import Auth
from silk_bookmark.settings import get_secret

#API Unsplash settings
client_id = get_secret("client_id")
client_secret = get_secret("client_secret")
redirect_uri = get_secret("redirect_uri")
code = ""

unsplash_auth = Auth(client_id, client_secret, redirect_uri, code=code)
unsplash_api = Api(unsplash_auth)