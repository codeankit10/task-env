from datetime import datetime,timedelta
from jose import JWTError,jwt
from . import schemas

key="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
algo="HS256"
token_exp=30

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=token_exp)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,key,algorithm=algo)
    return encode_jwt

def verify_token(token:str,cred_exception):
    try:
        payload=jwt.decode(token,key,algorithms=[algo])
        email:str=payload.get("sub")
        if email is None:
            raise cred_exception
        token_data=schemas.TokenData(email=email)
    except JWTError:
     raise cred_exception

