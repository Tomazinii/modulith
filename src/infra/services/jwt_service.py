from typing import Dict
from src.domain.services.interface import JwtServiceInterface
from src.domain.entities import Users
import jwt
import settings


class JwtService(JwtServiceInterface):
    
    def create_token(self, user: Users, key = settings.SIGNING_KEY, algorithm = "HS256",life_time_access_token = settings.ACCESS_TOKEN_EXPIRATION,life_time_refresh_token = settings.REFRESH_TOKEN_EXPIRATION) -> Dict[str, str]:

        access_payload = vars(user)
        access_payload["exp"] = life_time_access_token

        refresh_payload = vars(user)
        refresh_payload = {"exp": life_time_refresh_token}

        access_token = jwt.encode(payload=access_payload, key=key,algorithm=algorithm)
        refresh_token = jwt.encode(payload=refresh_payload, key=key, algorithm=algorithm)

        return {"access":access_token, "refresh":refresh_token}
    
    def refresh_token(self, refresh_token) -> str:

            


        return super().refresh_token()
    
    def verify_token(self):
        return super().verify_token()