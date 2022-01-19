#!/usr/bin/Python
# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS


###当前文件路径
d = path.dirname(__file__)

# Read the whole text.
file = open(path.join(d, '四阶段.txt'), encoding='utf-8').read()
##进行分词
#刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
default_mode =jieba.cut(file)
text = " ".join(default_mode)
alice_mask = np.array(Image.open(path.join(d, "1.png")))
stopwords = set(STOPWORDS)
file1 = open(path.join(d, 'stopwords.txt'), encoding='utf-8').read()
b = file1.split("\n")
for word in b:
    stopwords.add(word)
wc = WordCloud(
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white",   
    max_words=2000,   
    mask=alice_mask,  
    stopwords=stopwords)  
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "四阶段.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()