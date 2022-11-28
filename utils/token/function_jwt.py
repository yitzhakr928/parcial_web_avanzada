from jwt import encode, decode, exceptions
from os import  getenv
from flask import jsonify
from datetime import datetime,timedelta

def expire_date(days:int):
    now = datetime.now()
    new_date = now +timedelta(days)
    return new_date

 
def write_token(data: dict):
    token = encode(payload={**data, "exp":expire_date(1)}, key="1143153916", algorithm="HS256")
    return token.encode("UTF-8")


def valida_token(token, output=False):
    try:
         if output:
            return decode(token,  key="1143153916", algorithms=["HS256"])
         decode(token,  key="1143153916", algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid token"})
        response.status_code = 401
        return response
    except  exceptions.ExpiredSignatureError:
        response = jsonify({"message": "token is expired"})
        response.status_code = 401
        return response
