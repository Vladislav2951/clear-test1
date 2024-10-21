from clearml import Task
import os

# Инициализация задачи ClearML
task = Task.init(project_name="My Project", task_name="Run JupyterLab in Docker")

# Запуск JupyterLab
os.system("jupyter-lab --ip=0.0.0.0 --allow-root --no-browser")
