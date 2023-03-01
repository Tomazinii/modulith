import datetime
import time
import jwt

import secrets




key = secrets.token_hex(50)


class User:
    def __init__(self,nome) -> None:
        self.nome = nome



payload = {
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=1),
    "user":"alecrin",
    "user":"alecrin",
}

time.sleep(5)

encoded = jwt.encode(payload, key, algorithm="HS256")


print("testeasdsadsadasdasds", encoded)

decoded = jwt.decode(encoded, key, algorithms=['HS256'])

print(decoded)


class T:
    def __init__(self,nome) -> None:
        self.nome = nome



