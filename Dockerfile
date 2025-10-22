FROM python:3.12-slim  # 基于 Python 3.12 精简镜像构建
WORKDIR /app  # 设置工作目录为 /app
COPY requirements.txt .  # 复制依赖清单到工作目录
RUN pip install -r requirements.txt  # 安装依赖
COPY . .  # 复制所有文件到工作目录
CMD ["python", "app.py"]  # 容器启动命令，运行应用
