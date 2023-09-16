# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai 
# @contact: lianmingjie@shanda.com
# @file: model_eval_ensemble.py
# @time: 2023/9/14 22:50
import json
from collections import defaultdict, Counter

from sklearn.metrics import accuracy_score

file_list = ["Baichuan2-13b-base_eval.json", "LLAMA2-13B_eval.json", "XVERSE-13B_eval.json"]
# file_list = file_list[2:]

pred_labels_dict = defaultdict(list)
for file in file_list:
    with open(file, "r") as f:
        label_dict = json.loads(f.read())
    true_labels, pred_labels = label_dict["true_labels"], label_dict["pred_labels"]
    for i, label in enumerate(pred_labels):
        pred_labels_dict[str(i)].append(label)

pred_labels_final = []
for i in range(len(pred_labels_dict)):
    counter = Counter(pred_labels_dict[str(i)])
    if len(counter) != 1:
        print(i, counter)
    label_final = counter.most_common(n=1)[0][0]
    pred_labels_final.append(label_final)

print(accuracy_score(true_labels, pred_labels_final))

