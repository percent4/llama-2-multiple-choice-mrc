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

### 评估实验

调参，结果如下：

| model             | lr   | num_train_epochs | max_seq_length | accuracy |
|-------------------|------|------------------|----------------|--|
| llama-2-7b        | 1e-4 | 3                | 384            | 0.8691 |
| llama-2-7b        | 1e-4 | 3                | 320            | 0.8593 |
| llama-2-7b        | 1e-4 | 5                | 384            | 0.8545 |
| llama-2-7b        | 1e-4 | 5                | 320            | 0.8538 |
| llama-2-13b       | 1e-4 | 3                | 384            | 0.8851 |
| Baichuan-7b       | 2e-4 | 3                | 384            | 0.8357 |
| Baichuan-13b-chat | 1e-4 | 3                | 384            | 0.8726 |



### 测试

随机测试文章网址：[https://yingyu.xdf.cn/201901/10843790.html](https://yingyu.xdf.cn/201901/10843790.html)

文章:

```
Edward rose early on the New-year morning. He looked in every room and wished a Happy New Year to his family. Then he ran into the street to repeat that to those he might meet.

When he came back, his father gave him two bright, new silver dollars.

His face lighted up as he took them. He had wished for a long time to buy some pretty books that he had seen at the bookstore.

He left the house with a light heart, expecting to buy the books. As he ran down the street, he saw a poor family.

“I wish you a Happy New Year.” said Edward, as he was passing on. The man shook his head.

“You are not from this country.” said Edward. The man again shook his head, for he could not understand or speak his language. But he pointed to his mouth and to the children shaking with cold, as if (好像) to say, “These little ones have had nothing to eat for a long time.”

Edward quickly understood that these poor people were in trouble. He took out his dollars and gave one to the man, and the other to his wife.

They were excited and said something in their language, which doubtless meant, “We thank you so much that we will remember you all the time.”

When Edward came home, his father asked what books he had bought. He hung his head a moment, but quickly looked up.

“I have bought no books”, said he. “I gave my money to some poor people, who seemed to be very hungry then.” He went on, “I think I can wait for my books till next New Year.”

“My dear boy,” said his father, “here are some books for you, more as a prize for your goodness of heart than as a New-year gift”

“I saw you give the money cheerfully to the poor German family. It was nice for a little boy to do so. Be always ready to help others and every year of your life will be to you a Happy New Year.”
```

问题：

```
48. Edward expected to _________ with the money he got from his father.

A. help the poor family B. buy something to eat

C. buy some pretty books D. learn another language

49. Why did the poor man shake his head when Edward spoke to him?

A. He couldn’t understand the boy B. He wouldn’t accept the money

C. He didn’t like the boy’s language D. He was too cold to say anything

50. How much did Edward give the poor family?

A. One dollar B. Two dollars C. Three dollars D. Four dollars

51. We know that Edward_________ from the passage?

A. got a prize for his kind heart B. had to buy his books next year

C. bought the books at the bookstore D. got more money from his father
```

模型给出答案为： `CABA`