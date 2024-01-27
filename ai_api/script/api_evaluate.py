from fastapi import FastAPI
from pydantic import BaseModel
from petshop_ai import *
app = FastAPI()

# 创建一个模型来定义请求的结构
class RequestModel(BaseModel):
    message: str

# 创建一个路由
@app.post("/get_evaluate/")
async def request_evaluate(request_model: RequestModel):
    print(request_model.message)
    user_evaluate = get_evaluate(request_model.message)
    return {"user_rating": user_evaluate['评分'],"user_comments": user_evaluate['评语']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
