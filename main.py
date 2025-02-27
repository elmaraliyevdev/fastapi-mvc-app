from fastapi import FastAPI
from app.api.routes import auth, posts
from app.core.database import engine, Base

# Initialize DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MVC App")

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MVC App"}