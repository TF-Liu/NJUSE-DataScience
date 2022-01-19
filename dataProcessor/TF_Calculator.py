import os
import codecs
import math
import operator
import jieba


def fun(filepath):  # 遍历文件夹中的所有文件，返回文件list
    arr = []
    for root, dirs, files in os.walk(filepath):
        for fn in files:
            arr.append(root + "\\" + fn)
    return arr


def wry(txt, path):  # 写入txt文件
    f = codecs.open(path, 'a', 'utf8')
    f.write(txt)
    f.close()
    return path


def read(path):  # 读取txt文件，并返回list
    f = open(path, encoding="utf8")
    data = []
    for line in f.readlines():
        data.append(line)
    return data


def toword(path):  # 将一片文章使用jieba分词，返回list
    txt = open(path, "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    return words


def getstopword(path):  # 获取停用词表
    swlis = []
    for i in read(path):
        outsw = str(i).replace('\n', '')
        swlis.append(outsw)
    return swlis


def getridofsw(lis, swlist):  # 去除文章中的停用词
    afterswlis = []
    for i in lis:
        if str(i) in swlist:
            continue
        else:
            afterswlis.append(str(i))
    return afterswlis


def freqword(wordlis):  # 统计词频，并返回字典
    freword = {}
    for i in wordlis:
        if str(i) in freword:
            count = freword[str(i)]
            freword[str(i)] = count + 1
        else:
            freword[str(i)] = 1
    return freword


def corpus(filelist, swlist):  # 建立语料库
    alllist = []
    for i in filelist:
        afterswlis = getridofsw(toword(str(i)), swlist)
        alllist.append(afterswlis)
    return alllist


def wordinfilecount(word, corpuslist):  # 查出包含该词的文档数
    count = 0  # 计数器
    for i in corpuslist:
        for j in i:
            if word in set(j):  # 只要文档出现该词，这计数器加1，所以这里用集合
                count = count + 1
            else:
                continue
    return count


def tf_idf(wordlis, filelist, corpuslist):  # 计算TF-IDF,并返回字典
    outdic = {}
    tf = 0
    idf = 0
    dic = freqword(wordlis)
    outlis = []
    for i in set(wordlis):
        tf = dic[str(i)] / len(wordlis)  # 计算TF：某个词在文章中出现的次数/文章总词数
        # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
        idf = math.log(len(filelist) / (wordinfilecount(str(i), corpuslist) + 1))
        tfidf = tf * idf  # 计算TF-IDF
        outdic[str(i)] = tfidf
    orderdic = sorted(outdic.items(), key=operator.itemgetter(
        1), reverse=True)  # 给字典排序
    return orderdic


def tf(wordlis, filelist, corpuslist):  # 计算TF,并返回字典
    outdic = {}
    tf = 0
    dic = freqword(wordlis)
    outlis = []
    for i in set(wordlis):
        tf = dic[str(i)] / len(wordlis)  # 计算TF：某个词在文章中出现的次数/文章总词数
        outdic[str(i)] = tf
    orderdic = sorted(outdic.items(), key=operator.itemgetter(
        1), reverse=True)  # 给字典排序
    return orderdic


def befwry(lis):  # 写入预处理，将list转为string
    outall = ''
    for i in lis:
        ech = str(i).replace("('", '').replace("',", '\t').replace(')', '')
        outall = outall + '\t' + ech + '\n'
    return outall


def main():
    swpath = r'stopwords.txt'  # 停用词表路径
    swlist = getstopword(swpath)  # 获取停用词表列表

    filepath = r'corpus'
    filelist = fun(filepath)  # 获取文件列表

    wrypath = r'总TF.txt'

    corpuslist = corpus(filelist, swlist)  # 建立语料库

    outall = ''

    for i in filelist:
        afterswlis = getridofsw(toword(str(i)), swlist)  # 获取每一篇已经去除停用的词表
        tfdic = tf(afterswlis, filelist, corpuslist)  # 计算TF

        titleary = str(i).split('\\')
        title = str(titleary[-1]).replace('utf8.txt', '')
        echout = title + '\n' + befwry(tfdic)
        print(title + ' is ok!')
        outall = outall + echout
    print(wry(outall, wrypath) + ' is ok!')


if __name__ == '__main__':
    main()
