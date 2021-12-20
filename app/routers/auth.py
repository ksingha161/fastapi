from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas, models, utils
from .. import database, oauth2

router = APIRouter()

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(database.get_db)):
    # oauth only returns username and password in a dict that is why we do
    # models.User.email == user_credentials.username 
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
        'invalid credentials')
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
        'invalid credentials')

    # create a token and return token
    access_token = oauth2.create_access_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'bearer'}            