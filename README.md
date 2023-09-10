本项目使用LLAMA-2模型对多项选择阅读理解任务（Multiple Choice MRC）进行微调，取得了显著的进步。

### Author

- Jclian91(jclian91@126.com)

### Multiply Choice MRC

Multiply Choice MRC，属于MRC。常见的形式为阅读文章，针对问题和给出的多个选项（一般4个），确定答案是其中的一个选项，即我们在英语考试时的阅读理解。

本项目使用的数据集为[RACE](https://huggingface.co/datasets/race)，是Multiply Choice MRC中的经典数据集。

该数据集的Leaderboard网址为：[https://paperswithcode.com/dataset/race](https://paperswithcode.com/dataset/race) .

### 模型训练

训练框架为[Firefly](https://github.com/yangjianxin1/Firefly)，版本号参考`requiments.txt` .

本项目使用LLAMA-2-7b模型对RACE数据集进行微调，不做任何参数调优，在middle test数据集上的结果如下：

```bash
           A     0.9191    0.8091    0.8606       309
           B     0.8925    0.8557    0.8737       388
           C     0.8184    0.9278    0.8697       374
           D     0.8668    0.8740    0.8704       365

    accuracy                         0.8691      1436
   macro avg     0.8742    0.8666    0.8686      1436
weighted avg     0.8724    0.8691    0.8690      1436
```