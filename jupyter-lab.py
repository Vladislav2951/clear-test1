from clearml import Task
import os

# Инициализация задачи ClearML
task = Task.init(project_name="My Project", task_name="Run JupyterLab in Docker")

# Настройка Docker-контейнера с установленным JupyterLab
task.set_base_docker("jupyter/base-notebook:latest")

# Запуск JupyterLab
os.system("jupyterlab --ip=0.0.0.0 --allow-root --no-browser")
