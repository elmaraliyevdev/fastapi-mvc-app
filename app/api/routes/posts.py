from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.post import PostCreate, PostResponse
from app.services.post_service import create_post, get_user_posts, delete_post
from app.api.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter()

MAX_POST_SIZE = 1 * 1024 * 1024  # 1MB limit

@router.post("/add", response_model=PostResponse)
def add_post(request: Request, post: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_POST_SIZE:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Post size exceeds 1MB limit")
    return create_post(db, post, current_user)

@router.get("/get", response_model=list[PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_user_posts(db, current_user)

@router.delete("/delete")
def remove_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_post(db, post_id, current_user)