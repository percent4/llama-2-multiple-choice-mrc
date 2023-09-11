# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: gradio_serving.py
# @time: 2023/9/11 14:45
import gradio as gr
from transformers import AutoTokenizer
import torch


import sys
sys.path.append("../../")
from component.utils import ModelUtils

# 使用合并后的模型进行推理
model_name_or_path = '/home/jclian91/experiment/Firefly/script/checkpoint/firefly-llama2-7b-qlora-sft-race-merge'
# 生成超参配置
max_new_tokens = 1
top_p = 0.9
temperature = 0.01
repetition_penalty = 1.0
device = 'cuda:0'
# 加载模型
model = ModelUtils.load_model(
    model_name_or_path,
    load_in_4bit=False,
    adapter_name_or_path=None
).eval()
tokenizer = AutoTokenizer.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
    # llama不支持fast
    use_fast=False if model.config.model_type == 'llama' else True
)
print(f"load model: {model_name_or_path}")


# Gradio app
def predict(passage, question, option1, option2, option3, option4):
    prefix = 'Read the following passage and questions, then choose the right answer from options, ' \
             'the answer should be one of A, B, C, D.\n\n'
    passage = f'<passage>:\n{passage}\n\n'
    question = f'<question>:\n{question}\n\n'
    option = f'<options>:\nA {option1}\nB {option2}\nC {option3}\nD {option4}\n\n'
    suffix = f"<answer>:\n"
    prompt = ''.join([prefix, passage, question, option, suffix])
    # get input ids
    input_ids = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).input_ids.to(device)
    bos_token_id = torch.tensor([[tokenizer.bos_token_id]], dtype=torch.long).to(device)
    eos_token_id = torch.tensor([[tokenizer.eos_token_id]], dtype=torch.long).to(device)
    input_ids = torch.concat([bos_token_id, input_ids, eos_token_id], dim=1)
    # model predict
    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids, max_new_tokens=max_new_tokens, do_sample=True,
            top_p=top_p, temperature=temperature, repetition_penalty=repetition_penalty,
            eos_token_id=tokenizer.eos_token_id
        )
    outputs = outputs.tolist()[0][len(input_ids[0]):]
    response = tokenizer.decode(outputs)
    response = response.strip().replace(tokenizer.eos_token, "").strip()
    return f"The answer is {response}."


with gr.Blocks() as demo:
    # 设置输入组件
    gr_passage = gr.Textbox(lines=3, placeholder="Passage", label="Passage")
    gr_question = gr.Textbox(lines=1, placeholder="question", label="question")
    gr_option1 = gr.Textbox(lines=1, placeholder="option1", label="option1")
    gr_option2 = gr.Textbox(lines=1, placeholder="option2", label="option2")
    gr_option3 = gr.Textbox(lines=1, placeholder="option3", label="option3")
    gr_option4 = gr.Textbox(lines=1, placeholder="option4", label="option4")
    # 设置输出组件
    answer = gr.Textbox(label="Answer")
    # 设置按钮
    greet_btn = gr.Button("Show me the answer")
    # 设置按钮点击事件
    greet_btn.click(fn=predict,
                    inputs=[gr_passage, gr_question, gr_option1, gr_option2, gr_option3, gr_option4],
                    outputs=answer)

demo.launch(share=True)
