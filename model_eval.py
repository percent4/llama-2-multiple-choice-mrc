# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: model_eval.py
# @time: 2023/9/10 19:15
import json
import requests
from sklearn.metrics import accuracy_score, classification_report


def get_response(inputs):
    url = "http://10.241.132.208:8877/firefly"

    payload = json.dumps({
        "inputs": inputs
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    output = response.json()["response"]
    return output


if __name__ == '__main__':
    model = "LLAMA2-13B-all-eval-middle.json"
    with open("./data/race_high_test.jsonl", 'r') as f:
        samples = f.readlines()

    true_labels, pred_labels = [], []
    for i, human_input in enumerate(samples):
        conv = json.loads(human_input.strip())
        req_input = conv["conversation"][0]["human"]
        label = conv["conversation"][0]["assistant"]
        true_labels.append(label)
        pred = get_response(req_input)
        pred_labels.append(pred)
        print(i+1, label, pred, label == pred)

    print(true_labels)
    print(pred_labels)
    print(classification_report(true_labels, pred_labels, digits=4))

    with open(f"{model}_eval.json", "w", encoding="utf-8") as f:
        f.write(json.dumps({"true_labels": true_labels, "pred_labels": pred_labels}, ensure_ascii=False, indent=4))

