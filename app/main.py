from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from . import schemas



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


    
# Connecting to a database
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='social_api', user='postgres', password="breezy360", cursor_factory=RealDictCursor)
        
        cursor = conn.cursor()
        print('Database connection was successful')
        break
    except Exception as error:
        print("Connecting to database failed")
        print('Error: ', error)
        time.sleep(2)
    

#dummy post data 
my_posts = [
    {"id": 1, "title": "title of first post", "content": "content of first post"},
    {"id": 2, "title": "favorite desert", "content":"I like ice-cream"}
    ]


# finding a post
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
# deleting a post
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return p

@app.get("/")
async def read_root():
    return {"message": "Brandon is the best programmer in the world!"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts 

# Creating a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # try:
    #     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    #     post = cursor.fetchone()
    #     return {"post_detail": post}
    
    # except Exception as error:
    #     return error
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id of {id} does not exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
        

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id of {id} does not exist")
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


@app.put('/posts/{id}')
def update_post(id: int, post: schemas.PostCreate,  db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id=%s RETURNING *""", (post.title, post.content, post.published, str(id)))
   
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    first_post = post_query.first()
    
    if first_post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id of {id} does not exist")
    
    post_query.update(post.dict(), synchronize_session=False)
    
    db.commit()
    
 
    return post_query.first()
    