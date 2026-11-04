"""
掌柜问数 - 后端服务入口
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.query_router import router as query_router

# 创建 FastAPI 应用
app = FastAPI(
    title="掌柜问数",
    description="基于自然语言处理与数据分析的智能数据服务系统",
    version="1.0.0",
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(query_router, prefix="/api", tags=["query"])


def main():
    """启动 FastAPI 服务"""
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
