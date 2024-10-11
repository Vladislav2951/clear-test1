from clearml import Task

task = Task.init(project_name="StableDiffusion-LoRA", task_name="train-lora", task_type=Task.TaskTypes.optimizer)

task.get_logger().report_scalar("loss", "train", iteration=1, value=0.5)

import time
for epoch in range(10):
    loss = epoch * 0.1
    task.get_logger().report_scalar("loss", "train", iteration=epoch, value=loss)
    time.sleep(1)
task.close()
