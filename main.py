from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import PlainTextResponse

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/echo-string")
def read_item(q: Union[str, None] = None):
    return q

@app.get("/html", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI HTML 示例</title>
        </head>
        <body>
            <h1>欢迎使用 FastAPI！</h1>
        </body>
    </html>
    """

@app.get("/text", response_class=PlainTextResponse)
def read_root():
    return """
    success
    """