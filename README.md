# 掌柜问数 - 环境搭建完成

## ✅ 已完成

1. **uv 项目初始化**
   - `pyproject.toml` - 项目配置与依赖声明
   - `uv.lock` - 依赖锁定文件
   - `.python-version` - Python 3.11.9

2. **虚拟环境** (`.venv/`)
   - 已安装全部依赖
   - FastAPI 0.128.0
   - LangChain 1.2.7
   - SQLAlchemy 2.0.46
   - 等等...

3. **项目入口**
   - `main.py` - FastAPI 服务入口

4. **`.gitignore` 配置**
   - 排除 `.venv/`、`logs/`、`__pycache__/` 等

---

## 📋 后续操作步骤

### 步骤 1：启动 Docker 中间件服务

```bash
cd E:/work_document/online_lesson/掌柜问数/project/data-agent/docker

# 启动 MySQL、Qdrant、Elasticsearch、Kibana、TEI 等服务
docker compose up -d

# 查看服务状态
docker ps
```

### 步骤 2：激活虚拟环境

```bash
cd E:/work_document/online_lesson/掌柜问数/project/data-agent

# Git Bash
source .venv/Scripts/activate

# CMD
.venv\Scripts\activate.bat

# PowerShell
.venv\Scripts\Activate.ps1
```

### 步骤 3：构建知识库

```bash
# 确保虚拟环境已激活
python -m app.scripts.build_meta_knowledge
```

### 步骤 4：启动后端服务

```bash
# 方式一：直接运行
python main.py

# 方式二：使用 fastapi dev（支持热重载）
fastapi dev
```

后端服务将运行在：http://127.0.0.1:8000

### 步骤 5：启动前端服务

```bash
cd E:/work_document/online_lesson/掌柜问数/project/date-agent-frontend

# 安装依赖（如果还没装）
npm install

# 启动开发服务器
npm run dev
```

前端将运行在：http://localhost:5173

### 步骤 6：访问测试

浏览器打开：http://localhost:5173/

测试问题：
- 统计华北地区销售总额
- 统计2025年各地区销售总额
- 统计2025年各个商品的销量
- 统计各地区销量排名前三的商品

---

## 🔧 Git 操作

### 首次提交

```bash
cd E:/work_document/online_lesson/掌柜问数/project/data-agent

# 查看状态（确认 .venv 被忽略）
git status

# 添加所有文件
git add .

# 首次提交
git commit -m "init: 掌柜问数后端项目"

# 关联远程仓库
git remote add origin https://github.com/xiaoyey096-bit/-.git

# 推送
git branch -M main
git push -u origin main
```

---

## 📁 项目结构

```
data-agent/
├── .venv/              # 虚拟环境（已 gitignore）
├── app/                # 代码目录
│   ├── agent/          # 智能体
│   ├── api/            # 接口
│   ├── clients/        # 数据库客户端
│   ├── conf/           # 配置类
│   ├── core/           # 基础设施
│   ├── models/         # 数据库实体类
│   ├── prompt/         # 提示词工具
│   ├── repositories/   # Repo层
│   ├── scripts/        # 脚本
│   └── services/       # Service层
├── conf/               # 配置文件
│   ├── app_config.yaml
│   └── meta_config.yaml
├── docker/             # Docker 配置
├── prompts/            # 提示词目录
├── logs/               # 日志目录（已 gitignore）
├── main.py             # 后端入口
├── pyproject.toml      # 项目配置
├── uv.lock             # 依赖锁定
├── .python-version     # Python 版本
└── .gitignore          # Git 忽略配置
```

---

## ⚠️ 注意事项

1. **配置文件中的 API Key**
   - `conf/app_config.yaml` 中包含 DeepSeek API Key
   - 如果要提交到公开仓库，建议将其移到环境变量

2. **Docker 服务**
   - 确保 Docker Desktop 已启动
   - 服务端口：MySQL(3306)、Qdrant(6333)、ES(9200)、Kibana(5601)、TEI(8081)

3. **虚拟环境**
   - 已配置 `.gitignore`，`.venv/` 不会被提交
   - 其他人拉取代码后，运行 `uv sync` 即可恢复环境
