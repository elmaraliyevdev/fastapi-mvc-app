from pydantic import BaseModel, ConfigDict

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
