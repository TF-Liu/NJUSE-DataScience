import pygal

time = ["第一阶段", '第二阶段', '第三阶段', '第四阶段']


#将json数据添加到一个列表中
filename = '愤怒.json'

num = [0.01644738116335296/0.16408798950745768, 0.011967296268274004/0.15946956647179986,
       0.01678502701392582/0.19037233688424918, 0.012622158486806135/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '愤怒的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('愤怒的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '期待.json'

num = [0.024460610263723582/0.16408798950745768, 0.025013442295706307/0.15946956647179986,
       0.02726719032508017/0.19037233688424918, 0.023759430675681415/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '期待的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('期待的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '厌恶.json'

num = [0.013572759718985361/0.16408798950745768, 0.011120851373853933/0.15946956647179986,
       0.014412029248843902/0.19037233688424918, 0.011888749342981748/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '厌恶的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('厌恶的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '恐惧.json'

num = [0.025235624092711056/0.16408798950745768, 0.024221346071685253/0.15946956647179986,
       0.028270147480355168/0.19037233688424918, 0.021987647770158457/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '恐惧的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('恐惧的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '快乐.json'

num = [0.017192359342795827/0.16408798950745768, 0.02068681132459972/0.15946956647179986,
       0.026330403542655034/0.19037233688424918, 0.02581595073808458/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '快乐的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('快乐的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '悲伤.json'

num = [0.018235267739131342/0.16408798950745768, 0.019309912323218315/0.15946956647179986,
       0.022693506884809582/0.19037233688424918, 0.01853582578790335/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '悲伤的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('悲伤的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '惊讶.json'

num = [0.011817562964401033/0.16408798950745768, 0.013531242836503397/0.15946956647179986,
       0.016432577204619873/0.19037233688424918, 0.01344336055993459/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '惊讶的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('惊讶的心态频率随时间的变化.svg')

#将json数据添加到一个列表中
filename = '信任.json'

num = [0.037126424222356506/0.16408798950745768, 0.03361866397795893/0.15946956647179986,
       0.03818145518395961/0.19037233688424918, 0.035147544388521634/0.16320066775007191]

#创建折线图实例
line_chart = pygal.Line(x_label_rotation=0, show_minor_x_labels=True)
#标题
line_chart.title = '信任的心态频率随时间的变化'
#X轴数据
line_chart.x_labels = list(time)
#X轴坐标隔400显示一次
N = 1
line_chart.x_labels_major = time[::N]
#添加Y轴信息
line_chart.add('心态频率', num)
line_chart.render_to_file('信任的心态频率随时间的变化.svg')
