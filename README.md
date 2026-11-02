# 现代化学生信息管理系统

本仓库保留 Python/JSON 终端版学习项目，并新增独立的 FastAPI + MySQL + Docker 后端（`backend/`），两者数据不自动同步。

## 后端启动

1. 安装并启动 Docker Desktop。
2. 复制 `.env.example` 为 `.env`，修改两个数据库密码。
3. 在仓库根目录运行 `docker compose up --build -d`。
4. 执行初始迁移：`docker compose exec api alembic -c alembic.ini upgrade head`。
5. 访问 `http://localhost:8000/docs` 查看接口文档。

健康检查：`/health/live` 和 `/health/ready`。停止服务运行 `docker compose down`，MySQL 数据保留在命名卷；只有要清空数据时才用 `docker compose down -v`。

首版接口包含班级创建/列表/删除和学生增删改查、分页、按班级过滤。班级应先创建；学号全局唯一；仍有学生的班级不可删除。专业只保存在班级数据中。API 路径前缀为 `/api/v1`。

## 终端版模块

- 学生：`students/`
- 班级：`classes/`
- 课程：`courses/`
- 成绩：`scores/`
- 统计报表：`reports/`
- AI 成绩分析：`ai_analysis/`

`app.py` 为旧终端版入口。`backend/` 使用独立依赖清单和 Alembic 迁移，不复用旧版硬编码数据库配置。
