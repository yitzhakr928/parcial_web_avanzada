from jwt import encode, decode, exceptions
from os import  getenv
from datetime import datetime

def expire_date(days:int):
    now = datetime.now()
    new_date = now + datetime.timedelta(days)
    return new_date


def write_token(data: dict):
    token= encode(payload={**data, "exp":expire_date(1)}, key=getenv("SECRET"), algorithm="HS256")
    return token.encode("UTF-8")


def valida_token(token, output=False):
    try:
         if output:
            return decode(token,  key=getenv("SECRET"), algorithms=["HS256"])
         decode(token,  key=getenv("SECRET"), algorithms=["HS256"])
        
    except exceptions.DecodeError:
        
        pass
