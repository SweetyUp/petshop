from fastapi import FastAPI
from pydantic import BaseModel
from petshop_ai import *
app = FastAPI()

# 创建一个模型来定义请求的结构
class RequestModel(BaseModel):
    message: str

# 创建一个路由
@app.post("/get_pet/")
async def request_pet(request_model: RequestModel):
    print(request_model.message)
    pet_info = get_pet(request_model.message)
    return pet_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
