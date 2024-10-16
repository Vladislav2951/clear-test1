import transformers
import torch
from clearml import Task

task = Task.init(project_name="ИКТНС", task_name="QWEN")

model_id = "Qwen/Qwen2.5-7B-Instruct"

model = transformers.AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    device_map="auto"
)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)

prompt = "Привет, как твои дела сегодня?"
inputs = tokenizer(prompt, return_tensors="pt")

input_ids = inputs.input_ids.to(model.device)
attention_mask = inputs.attention_mask.to(model.device)

with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    logits = outputs.logits[:, -1, :]
    probs = torch.nn.functional.softmax(logits, dim=-1)

    if torch.isnan(probs).any() or torch.isinf(probs).any():
        raise ValueError("Вероятности содержат NaN или inf значения!")

generated_ids = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_new_tokens=100,
    temperature=0.7,
    top_k=50,
    top_p=0.9
)

generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

task.upload_artifact(name="Generated Text", artifact_object=generated_text)

task.close()
