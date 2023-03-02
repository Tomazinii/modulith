import datetime
import time
import jwt

import secrets




key = secrets.token_hex(50)


class User:
    def __init__(self,nome) -> None:
        self.nome = nome



payload = {
    "exp": datetime.datetime.utcnow(),
    "user":"alecrin",
    "user":"alecrin",
}


encoded = jwt.encode(payload, key, algorithm="HS256")



decoded = jwt.decode(encoded, key, algorithms=['HS256'])

print(decoded)





