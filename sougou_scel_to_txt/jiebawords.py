#-*- coding:utf-8 -*-
import jieba
import jieba.analyse
jieba.load_userdict('./sougou11.txt')
word_list = jieba.cut("今天天气真好。亲爱的，我们去远足吧！",cut_all=False)
print("|".join(word_list))
str="今天天气真好。亲爱的，\n我们去远足吧"
keywords = jieba.analyse.extract_tags(str, topK=None, withWeight=True)
for item in keywords:
    print(item[0],item[1])
print("")