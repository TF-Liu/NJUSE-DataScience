import csv
import re


def input_el():
    csv_file = csv.reader(open('Emotion Lexicon.csv', 'r', encoding="utf8"))
    emotion_lexicon = dict()
    for line in csv_file:
        if emotion_lexicon.get(line[0]) is None:
            emotion_lexicon[line[0]] = dict(type=[line[1]], strength=[float(line[2])])
        else:
            emotion_lexicon[line[0]]['type'].append(line[1])
            emotion_lexicon[line[0]]['strength'].append(float(line[2]))
    return emotion_lexicon


def input_tf():
    f = open("总TF.txt", 'r', encoding='UTF-8')
    TF = dict()
    for i in f.readlines():
        line = re.split('[\n\t ]', i)
        for c in line:
            if c == '':
                line.remove(c)
        if len(line) == 2:
            if TF.get(line[0]) is None:
                TF[line[0]] = float(line[1])
            else:
                TF[line[0]] += float(line[1])
    for item in TF:
        TF[item] = TF.get(item) / 4
    return TF


def mapping(emotion_lexicon, TF):
    emotion_map = dict(anger=0, anticipation=0, disgust=0, fear=0, joy=0, sadness=0, surprise=0, trust=0)
    for word in TF:
        for item in emotion_lexicon:
            if word == item:
                i = 0
                for emotion in emotion_lexicon.get(item)['type']:
                    emotion_map[emotion] += emotion_lexicon.get(item)['strength'][i] * TF.get(word)
                    i += 1
    return emotion_map


if __name__ == '__main__':
    emotion_lexicon = input_el()
    TF = input_tf()
    emotion_map = mapping(emotion_lexicon, TF)
    with open("总心态分布.txt", "w", encoding='UTF-8') as f:
        for item in emotion_map:
            f.write(item + "=" + str(emotion_map.get(item)) + "\n")
