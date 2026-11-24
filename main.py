"""
掌柜问数 - 后端服务入口
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.query_router import query_router
from app.clients.embedding_client_manager import embedding_client_manager
from app.clients.es_client_manager import es_client_manager
from app.clients.mysql_client_manager import dw_mysql_client_manager, meta_mysql_client_manager
from app.clients.qdrant_client_manager import qdrant_client_manager
from app.core.log import logger

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


@app.on_event("startup")
async def startup_event():
    """应用启动时初始化所有客户端管理器"""
    logger.info("初始化客户端管理器...")
    embedding_client_manager.init()
    es_client_manager.init()
    qdrant_client_manager.init()
    dw_mysql_client_manager.init()
    meta_mysql_client_manager.init()
    logger.info("客户端管理器初始化完成")


@app.on_event("shutdown")
async def shutdown_event():
    """应用关闭时释放所有客户端管理器资源"""
    logger.info("关闭客户端管理器...")
    await es_client_manager.close()
    await qdrant_client_manager.close()
    await dw_mysql_client_manager.close()
    await meta_mysql_client_manager.close()
    logger.info("客户端管理器已关闭")


# 注册路由
app.include_router(query_router, tags=["query"])


def main():
    """启动 FastAPI 服务"""
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8001,
        reload=False,
    )


if __name__ == "__main__":
    main()
