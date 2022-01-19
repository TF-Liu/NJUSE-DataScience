import json
import pygal
from collections import Counter

#将json数据添加到一个列表中

filename = 'test.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)

time, dependency = [], []
for btc_dict in btc_data:
    time.append(btc_dict['publish_time'])
    dependency.append(int(btc_dict['dependency']))

time = list(reversed(time))
dependency = list(reversed(dependency))

#创建折线图实例，X轴标签顺时针旋转20度，不用显示所有X轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
#标题
line_chart.title = '不同时间下人民网的微博与疫情相关度的变化'
#X轴数据
line_chart.x_labels = time
#X轴坐标隔400显示一次
N = 400
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('相关度', dependency)
line_chart.render_to_file('不同时间下人民网的微博与疫情的相关度变化.svg')

filename = '2286908003.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)

up_num, retweet_num, comment_num = [], [], []
for btc_dict in btc_data["weibo"]:
    up_num.append(int(btc_dict['up_num']))
    retweet_num.append(int(btc_dict['retweet_num']))
    comment_num.append(int(btc_dict['comment_num']))
#创建折线图实例，X轴标签顺时针旋转20度，不用显示所有X轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
up_num.sort()
b = dict(Counter(up_num))
#标题
line_chart.title = '不同点赞数的人民网微博的条数'
#X轴数据
line_chart.x_labels = list(b.keys())
#X轴坐标隔400显示一次
N = 600
line_chart.x_labels_major = up_num[::N]
#添加Y轴信息
line_chart.add('条数', list(b.values()))
line_chart.render_to_file('不同点赞数的人民网微博的条数.svg')

#创建折线图实例，X轴标签顺时针旋转20度，不用显示所有X轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
retweet_num.sort()
b = dict(Counter(retweet_num))
#标题
line_chart.title = '不同转发数的人民网微博的条数'
#X轴数据
line_chart.x_labels = list(b.keys())
#X轴坐标隔20天显示一次
N = 800
line_chart.x_labels_major = retweet_num[::N]
#添加Y轴信息
line_chart.add('条数', list(b.values()))
line_chart.render_to_file('不同转发数的人民网微博的条数.svg')

#创建折线图实例，X轴标签顺时针旋转20度，不用显示所有X轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
comment_num.sort()
b = dict(Counter(comment_num))
#标题
line_chart.title = '不同评论数的人民网微博的条数'
#X轴数据
line_chart.x_labels = list(b.keys())
#X轴坐标隔20天显示一次
N = 800
line_chart.x_labels_major = comment_num[::N]
#添加Y轴信息
line_chart.add('条数', list(b.values()))
line_chart.render_to_file('不同评论数的人民网微博的条数.svg')