from fastapi import FastAPI
import uvicorn

from enum import Enum

app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {"message": "Hello World !!!"}

@app.get("/blog/all")
def all_blogs():
    return {"blogs": [{"blog1": "this is blog 1"}, {"blog2": "this is blog 2"}, {"blog3": "this is blog 3"}, {"blog4": "this is blogs 4"}]}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"BlogType": f"This is a {type} blog"}

@app.get("/blog/{id}")
def get_blog(id: int) -> str:
    return {f"blog{id}": f"this is blog{id}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
