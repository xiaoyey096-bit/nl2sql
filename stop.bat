@echo off
chcp 65001 >nul
echo ========================================
echo    掌柜问数 - 一键停止脚本
echo ========================================
echo.

REM 停止 Docker 容器
echo [1/2] 停止 Docker 服务...
cd /d "%~dp0..\docker"
docker compose down
echo [完成] Docker 服务已停止
echo.

REM 关闭前后端窗口
echo [2/2] 关闭前后端服务窗口...
taskkill /FI "WINDOWTITLE eq 掌柜问数-后端" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq 掌柜问数-前端" /F >nul 2>&1
echo [完成] 前后端服务已关闭
echo.

echo ========================================
echo    所有服务已停止
echo ========================================
echo.
pause
