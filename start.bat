@echo off
chcp 65001 >nul
echo ========================================
echo    掌柜问数 - 一键启动脚本
echo ========================================
echo.

REM 检查 Docker 是否运行
docker info >nul 2>&1
if errorlevel 1 (
    echo [错误] Docker 未运行，请先启动 Docker Desktop
    pause
    exit /b 1
)

REM 启动 Docker 容器
echo [1/3] 启动 Docker 服务...
cd /d "%~dp0..\docker"
docker compose up -d
if errorlevel 1 (
    echo [错误] Docker 服务启动失败
    pause
    exit /b 1
)
echo [完成] Docker 服务已启动
echo.

REM 启动后端服务
echo [2/3] 启动后端服务 (端口 8001)...
start "掌柜问数-后端" cmd /k "cd /d %~dp0 && uv run python main.py"
echo [完成] 后端服务已启动
echo.

REM 启动前端服务
echo [3/3] 启动前端服务 (端口 5173)...
start "掌柜问数-前端" cmd /k "cd /d %~dp0..\date-agent-frontend && npm run dev"
echo [完成] 前端服务已启动
echo.

echo ========================================
echo    启动完成！
echo    后端: http://localhost:8001
echo    前端: http://localhost:5173
echo ========================================
echo.
echo 按任意键关闭此窗口（服务将继续运行）
pause >nul
