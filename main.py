from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 
app=FastAPI()

@app.get('/post')  
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published post'}

    else:
        return {'data':f'{limit} post from db'}


@app.get('/post/unpublished')
def unpublished():
    return {'data':'all unpublished post'}

@app.get('/post/{id}')
def show(id:int):
    return {'data':id}

@app.get('/post/{id}/comments')
def comment(id,limit=10):
    return {'data':{'1','2'}}

class Post(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/post')
def creat_post(post:Post):
    return {'data':f"post created {post.title}"}
