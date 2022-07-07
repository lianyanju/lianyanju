from fastapi import FastAPI

import uvicorn

from pydantic import BaseModel, EmailStr

"""
    以最快的速度，快速建立启动一个http请求服务器 
    
"""

app = FastAPI(title="api_by_mocker", version="0.1.0")


@app.get("/")  # 接口的地址
async def read_root():
    return {"Hello": "World"}  # 响应结果


@app.get("/items/{item_id}")  # 接口的地址
async def read_item(item_id: int):
    return {"item_id": item_id}


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


#用postman 或者 代码 ，或者其他工具可以模拟post请求就可以进入到这里～
@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run(app="fake_mock_server:app", host="0.0.0.0", reload=False)
    #  本质：uvicorn是一个服务器
    #  1： 注意 这里的web 是py文件的命名
    #  2： 默认端口为 8000可以通过以下方式修改端口
    #       uvicorn.run(app, port=8000)

    #  3：默认 host 为 localhost
    #       uvicorn.run(app, host="*.*.*.*",)
    #  4：访问：http://127.0.0.1:8000/docs 可以访问swagger的api文档！！
    #  5：访问：http://127.0.0.1:8000/redoc可以访问另外一种格式的的api文档！！

