from sqlalchemy.orm import Session
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate
from fastapi import HTTPException, status
from cachetools import TTLCache

# In-memory cache (caches user posts for 5 minutes)
cache = TTLCache(maxsize=100, ttl=300)

def create_post(db: Session, post_data: PostCreate, user: User):
    post = Post(text=post_data.text, user_id=user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    cache.pop(user.id, None)  # Invalidate cache
    return post

def get_user_posts(db: Session, user: User):
    if user.id in cache:
        return cache[user.id]
    # Optimize query to avoid redundant DB calls
    posts = db.query(Post).filter(Post.user_id == user.id).all()
    cache[user.id] = posts
    return posts

def delete_post(db: Session, post_id: int, user: User):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(post)
    db.commit()
    cache.pop(user.id, None)  # Invalidate cache
    return {"message": "Post deleted successfully"}