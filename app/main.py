from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uvicorn
 
# 加载 .env 文件中的环境变量（仅本地开发时有用）
load_dotenv()
 
# 获取端口号，默认 3030
port = int(os.getenv("PORT", 3030))
 
# 创建 FastAPI 应用
app = FastAPI()
 
# 配置 CORS：允许任意来源，仅允许 GET 方法
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 允许所有域名
    allow_methods=["GET"], # 仅允许 GET 请求
    allow_headers=["*"],   # 允许所有请求头
)
 
# 定义 /products 路由
@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
 
# 启动服务
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
 