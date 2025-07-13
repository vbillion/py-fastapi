# FastAPI 示例项目
此项目为 FastAPI 基础应用示例，展示了不同类型 API 端点的实现。

# Installation
Create and activate a virtual environment and then install FastAPI:
```
$ python -m venv .venv
$ source .venv/bin/activate
$ which python
$ pip install "fastapi[standard]"
$ pip install "uvicorn[standard]"
```

# Run it
Run the server with:
```
# Development
$ fastapi dev main.py
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# Production
$ fastapi run main.py
```

# API 文档
FastAPI 自动生成交互式 API 文档，可通过以下链接访问：
Swagger UI：http://127.0.0.1:8000/docs
ReDoc：http://127.0.0.1:8000/redoc