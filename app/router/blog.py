from fastapi import APIRouter, Response, status
from pydantic import BaseModel

from typing import Optional 
from enum import Enum

router = APIRouter(prefix="/blog", tags=['blog'])

# @router.get("/all")
# def all_blogs():
#     return {"blogs": [{"blog1": "this is blog 1"}, {"blog2": "this is blog 2"}, {"blog3": "this is blog 3"}, {"blog4": "this is blogs 4"}]}

@router.get("//all")
def all_blogs(page=1, page_size: Optional[int] = None):
    return {"blog": f"this is blog's page {page} of size {page_size}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"BlogType": f"This is a {type} blog"}

@router.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response) -> str:
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"blog": "", "error": "Not Found"}
    else:
        return {f"blog{id}": f"this is blog{id}"}

@router.get("/blog/{id}/comment/{comment_id}", tags=['comment'],
         summary='Get comment of a blog')
def get_blog_by_id_comment_id(id: int, comment_id: int, is_valid: bool = True, username: Optional[str] = None):
    """
    # This function simulates the retrival of a comment from a blog. #
    - **id** path parameter blog id
    - **comment_id** path parameter id of the comment
    - **is_valid** query parameter boolean flag indicating if the comment is active of not
    - **username** query parameter optional 

    """
    return {"blog": f"this is blog {id} , with comment {comment_id} - status : {is_valid}, by username: {username}"}

class BlogModel(BaseModel):
    title: str
    type: BlogType
    content: str


@router.post("/create", status_code=201, summary='create blog')
def create_blog(blog: BlogModel):
    """
    API simulation to create a new blog post
    - **blog_name** (query parameter) name of the blog
    - **type** (query parameter) type of the blog
    - **blog_text**
    """
    return {"data": blog}
