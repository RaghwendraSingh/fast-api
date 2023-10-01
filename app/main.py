from fastapi import FastAPI, Response, status
import uvicorn

from router import blog

from typing import Optional 
from enum import Enum

app = FastAPI(debug=True)
app.include_router(blog.router)

@app.get("/", status_code=status.HTTP_200_OK, tags=['health'], summary='Returns health of the application')
def health():
    return {"status": "Healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
