from unsplash.api import Api
from unsplash.auth import Auth

#api Unsplash settings
client_id = "b6332c936c260748d8f18b804170f6ad86d8f9e3d2079cebb17c2d485b43d222"
client_secret = "299ed1ba374d08f4ce76044d94a69345022e329d55e7ce84f85d7dca282c503b"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)