#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import jieba
import pandas as pd
import numpy
import time


Starttime = time.time()


def fenxi(Lists):
    content_S = []
    for each in Lists:
        each = str(each)
        each = each.strip('()')  # 删除2边括号
        each = jieba.lcut(each)
        if len(each) > 1 and each != '\r\n':
            content_S.append(each)
    return content_S

db = pymysql.connect('localhost', 'root', '', 'test', charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT bz from zlzp_new WHERE id < 300000")
Lists = cursor.fetchall()
db.close()
# print len(Lists)

content_S = fenxi(Lists)

df_content = pd.DataFrame({'content_S':content_S})
# print(df_content.head())
stopwords = pd.read_csv('stopwords.txt',index_col=False,sep='\t',quoting=3,names=['stopword'], encoding='utf-8')
# print(stopwords.head(20))


def drop_stopwords(contents,stopwords):
    contents_clean = []
    all_words = []
    for line in contents:
        line_clean = []
        for word in line:
            if word in stopwords:
                continue
            if word==' ':
                continue
            line_clean.append(word)
            all_words.append(str(word))
        contents_clean.append(line_clean)
    return contents_clean,all_words


contents = df_content.content_S.values.tolist()   #需要处理的文本
stopwords = stopwords.stopword.values.tolist()   #停用单词文本
contents_clean,all_words = drop_stopwords(contents,stopwords)  #contents处理后的文本 ，stopwords 被处理的单词
# print(contents)
# print(stopwords)
df_content = pd.DataFrame({'contents_clean':contents_clean})  #构造 新文本格式

df_all_words=pd.DataFrame({'all_words':all_words})     # 所有词语
# print(df_all_words.head())
# print(df_all_words)
#词频分析
#https://www.cnblogs.com/zephyr-1/p/5874678.html

words_count = df_all_words.groupby(df_all_words['all_words'])['all_words'].agg({'count':numpy.size})
words_count = words_count.reset_index().sort_values('count',ascending=False)
# print(words_count.head(100).values)
# words_count=words_count.reset_index().groupby(df_all_words['all_words']).agg('count')
# print(words_count.sort_values('count'))
# print(words_count)




from wordcloud import WordCloud
import matplotlib.pyplot as plt
# %matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
word_frequence = {x[0]:x[1] for x in words_count.head(100).values}
wordcloud=wordcloud.fit_words(word_frequence)
#
# print(wordcloud)


Stoptime = time.time()
Runtime = Stoptime-Starttime
print('程序运行时间: %s 秒'%(Runtime))

plt.imshow(wordcloud)
# plt.axis('off')
plt.show()
# print(plt.imshow(wordcloud))

