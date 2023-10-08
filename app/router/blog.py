from fastapi import APIRouter, Response, status, Path, Query, Body
from pydantic import BaseModel

from typing import Optional, List, Dict
from enum import Enum

router = APIRouter(prefix="/blog", tags=['blog'])

# @router.get("/all")
# def all_blogs():
#     return {"blogs": [{"blog1": "this is blog 1"}, {"blog2": "this is blog 2"}, {"blog3": "this is blog 3"}, {"blog4": "this is blogs 4"}]}

@router.get("/all")
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

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    type: BlogType
    content: str
    publisher: Optional[bool]
    tags: List[str]
    metadata: Dict[str, str]
    image: Optional[Image]


@router.post("/create", status_code=201, summary='create blog')
def create_blog(blog: BlogModel ):
    """
    API simulation to create a new blog post
    - **blog_name** (query parameter) name of the blog
    - **type** (query parameter) type of the blog
    - **blog_text**
    """
    return {"data": blog}

@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogModel, id: int, 
                   comment_title: str = Query(
                       None, title="Id of the comment", 
                       description="Some description for comment id",
                       alias='commentTitle',
                       deprecated=True),
                    content: str = Body(...,
                                   min_length=0,
                                   max_length=50,
                                   regex='^[a-z\s]*$'),
                    version: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
                    comment_id: int = Path(None, gt=5, le=10)):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'comment_id': comment_id,
        'version': version
    }

def required_functionality():
    return {"message": "learning fastapi is important"}