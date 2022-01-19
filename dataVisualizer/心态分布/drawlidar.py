import json

import pygal

filename = '第一阶段心态分布.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)



# 调用Radar这个类，并设置雷达图的填充，及数据范围
radar_chart = pygal.Radar(fill=True, range=(0, 0.3))
# 添加雷达图的标题
radar_chart.title = '第一阶段心态分布'
# 添加雷达图各顶点的含义
radar_chart.x_labels = list(btc_data.keys())

sum = 0
for value in list(btc_data.values()):
    sum += value
print(sum)

b = []
for value in list(btc_data.values()):
    b.append(value / sum)

# 绘制两条雷达图区域
radar_chart.add('心态频率', b)

# 保存图像
radar_chart.render_to_file('第一阶段心态分布.svg')
f.close()

filename = '第二阶段心态分布.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)



# 调用Radar这个类，并设置雷达图的填充，及数据范围
radar_chart = pygal.Radar(fill=True, range=(0, 0.3))
# 添加雷达图的标题
radar_chart.title = '第二阶段心态分布'
# 添加雷达图各顶点的含义
radar_chart.x_labels = list(btc_data.keys())

sum = 0
for value in list(btc_data.values()):
    sum += value
print(sum)

b = []
for value in list(btc_data.values()):
    b.append(value / sum)

# 绘制两条雷达图区域
radar_chart.add('心态频率', b)

# 保存图像
radar_chart.render_to_file('第二阶段心态分布.svg')
f.close()

filename = '第三阶段心态分布.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)



# 调用Radar这个类，并设置雷达图的填充，及数据范围
radar_chart = pygal.Radar(fill=True, range=(0, 0.3))
# 添加雷达图的标题
radar_chart.title = '第三阶段心态分布'
# 添加雷达图各顶点的含义
radar_chart.x_labels = list(btc_data.keys())

sum = 0
for value in list(btc_data.values()):
    sum += value
print(sum)

b = []
for value in list(btc_data.values()):
    b.append(value / sum)

# 绘制两条雷达图区域
radar_chart.add('心态频率', b)

# 保存图像
radar_chart.render_to_file('第三阶段心态分布.svg')
f.close()

filename = '第四阶段心态分布.json'
with open(filename, encoding='utf-8') as f:
    btc_data = json.load(f)



# 调用Radar这个类，并设置雷达图的填充，及数据范围
radar_chart = pygal.Radar(fill=True, range=(0, 0.3))
# 添加雷达图的标题
radar_chart.title = '第四阶段心态分布'
# 添加雷达图各顶点的含义
radar_chart.x_labels = list(btc_data.keys())

sum = 0
for value in list(btc_data.values()):
    sum += value
print(sum)

b = []
for value in list(btc_data.values()):
    b.append(value / sum)

# 绘制两条雷达图区域
radar_chart.add('心态频率', b)

# 保存图像
radar_chart.render_to_file('第四阶段心态分布.svg')
f.close()