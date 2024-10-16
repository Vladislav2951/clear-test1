import transformers
import torch
from clearml import Task

task = Task.init(project_name="ИКТНС", task_name="Meta-Llama-3.1")

model_id = "meta-llama/Meta-Llama-3.1-8B"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.float16}, device_map="auto"
)

result = pipeline("Привет, как твои дела сегодня?", max_new_tokens=100)


task.upload_artifact(name="Generated Text", artifact_object=result[0]['generated_text'])

task.close()