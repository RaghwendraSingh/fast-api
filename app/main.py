from fastapi import FastAPI, Response, status
import uvicorn

from typing import Optional 
from enum import Enum

app = FastAPI(debug=True)

@app.get("/", status_code=status.HTTP_200_OK, tags=['health'], summary='Returns health of the application')
def health():
    return {"status": "Healthy"}

# @app.get("/blog/all")
# def all_blogs():
#     return {"blogs": [{"blog1": "this is blog 1"}, {"blog2": "this is blog 2"}, {"blog3": "this is blog 3"}, {"blog4": "this is blogs 4"}]}

@app.get("/blog/all", tags=['blog'])
def all_blogs(page=1, page_size: Optional[int] = None):
    return {"blog": f"this is blog's page {page} of size {page_size}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get("/blog/type/{type}", tags=['blog'])
def get_blog_type(type: BlogType):
    return {"BlogType": f"This is a {type} blog"}

@app.get("/blog/{id}", status_code=status.HTTP_200_OK
         , tags=['blog'])
def get_blog(id: int, response: Response) -> str:
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"blog": "", "error": "Not Found"}
    else:
        return {f"blog{id}": f"this is blog{id}"}

@app.get("/blog/{id}/comment/{comment_id}", tags=['blog', 'comment'],
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
