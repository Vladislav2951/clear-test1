from clearml import Task
import os

# Инициализация задачи ClearML
task = Task.init(project_name="My Project", task_name="Run JupyterLab in Docker")

# Настройка Docker-контейнера с установленным JupyterLab
task.set_base_docker("jupyter/base-notebook:latest")

# Запуск задачи на удаленном агенте (при использовании ClearML агент будет запускать задачу внутри Docker)
task.execute_remotely(queue_name="default", exit_process=False)

# Запуск JupyterLab
os.system("jupyter lab --ip=0.0.0.0 --allow-root --no-browser")
