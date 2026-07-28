from fastapi import APIRouter, Depends
from app.api.v1.deps import get_current_user
from app.schemas import UserOut

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_current_user(current_user = Depends(get_current_user)):
    return current_user
