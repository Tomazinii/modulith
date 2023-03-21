from typing import Dict

import json
from src.domain.services.interface import JwtServiceInterface
from src.domain.entities import Users
import jwt
from core.base import settings


class JwtService(JwtServiceInterface):
    
    @staticmethod
    def create_token(user: Users, key = settings.SIGNING_KEY, algorithm = "HS256",life_time_access_token = settings.ACCESS_TOKEN_EXPIRATION,life_time_refresh_token = settings.REFRESH_TOKEN_EXPIRATION) -> Dict[str, str]:
        """ this method create token to user in dict format -> {token, refresh_token} """

        access_payload = vars(user)  # esses dados nao podem ser passados dessa maneira. Antes precisam ser filtrados; password nao pode ser passada. Solução é criar um serializer
        if type(access_payload["password"]) is bytes:
            access_payload["password"] = user.password.decode() # resolba esse problema

        access_payload["exp"] = life_time_access_token
        refresh_payload = vars(user)
        refresh_payload = {"exp": life_time_refresh_token}
        del access_payload["_sa_instance_state"] # enteder pq o elemento está sendo gerado e corrigir

        access_token = jwt.encode(payload=access_payload, key=key,algorithm=algorithm)
        refresh_token = jwt.encode(payload=refresh_payload, key=key, algorithm=algorithm)
        return {"access":access_token, "refresh":refresh_token}
    

    def refresh_token(self, refresh_token, key = settings.SIGNING_KEY,algorithm = "HS256", life_time_access_token = settings.ACCESS_TOKEN_EXPIRATION) -> str:
        """ this method create new_token from the refresh_token """
        try:
            payload = jwt.decode(refresh_token,key=key, algorithms=algorithm)
            payload["exp"] = life_time_access_token
            new_token = jwt.encode(payload=payload, key=key, algorithm=algorithm)
            return new_token
        except:
            raise Exception("token invalid or expired")
        
    
    def verify_token(self, token, algorithm = "HS256",key=settings.SIGNING_KEY) -> bool:
        """ this method verify if token is valid """
        try:
            jwt.decode(token,algorithms=[algorithm], key=key)

            return True
        except:
            raise Exception("token invalid or expired")