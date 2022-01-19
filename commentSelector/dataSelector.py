import json
import numpy as np

weibo_list = []
text = ['疫', '新冠', "新型冠状病毒", "肺炎", "确诊病例", "疑似病例", "患者", "隔离", "密切接触", "潜伏期", "人传人",
        "防控", "口罩", "医疗", "疫苗", "封城", "公共卫生事件", "传染", '方舱医院', '核酸', '消毒', '防控', '复工',
        '复产', '复学', '治愈']


def input_json():
    document = open("2656274875.json", encoding='utf-8')
    setting = json.load(document)
    for weibo in setting['weibo']:
        weibo_list.append(
            dict(id=weibo['id'], content=weibo['content'], publish_time=weibo['publish_time'],
                 comment_num=weibo['comment_num'], dependency=0, importance=0))


def calculate_dependency():
    for weibo in weibo_list:
        for word in text:
            if word in weibo['content']:
                weibo['dependency'] += 1


def calculate_importance():
    comment_num_list = []
    for weibo in weibo_list:
        comment_num_list.append(weibo['comment_num'])
    x = np.array(comment_num_list)
    mu = np.mean(x)
    for weibo in weibo_list:
        if weibo['comment_num'] > mu:
            weibo['importance'] = 1


def output_json():
    f = open('yangshixinwen.json', mode='w', encoding='utf-8')
    json.dump(weibo_list, f, indent=4, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    input_json()
    calculate_dependency()
    calculate_importance()
    output_json()
    # 以下代码可用于求符合条件的微博数量
    # count = 0
    # for weibo in weibo_list:
    #     if weibo['importance'] > 0 and weibo['dependency'] > 0:
    #         count += 1
    # print(count)
