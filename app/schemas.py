from pydantic import BaseModel

# Class to represent data models/schemas  
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
  
  
class PostCreate(PostBase):
    pass
  

class Post(BaseModel):
    title: str
    content: str
    published: bool

