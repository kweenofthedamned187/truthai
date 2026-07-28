from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.db import crud
from app.schemas import UserCreate, UserOut, Token
from app.api.v1.deps import get_db
from app.services import auth_service

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = auth_service.get_password_hash(user_in.password)
    user = crud.create_user(db, email=user_in.email, hashed_password=hashed)
    return user


@router.post("/login", response_model=Token)
def login(user_in: UserCreate, response: Response, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, user_in.email)
    if not user or not auth_service.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = auth_service.create_access_token(subject=user.id)
    # For now refresh token is a JWT as well; in production store in Redis for revocation and set as httpOnly cookie
    refresh_token = auth_service.create_access_token(subject=user.id, expires_delta=None)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=False, samesite="lax")
    return {"access_token": access_token, "token_type": "bearer"}
