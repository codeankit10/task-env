from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer

from .import token

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data:str=Depends(oauth2_scheme)):
    cred_except=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate",
        headers={"WWW-Authenticate": "Bearer"}

    )

    return token.verify_token(data,cred_except)
    