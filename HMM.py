import nltk
import random
import jieba
#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#cut = list(jieba.cut(s, cut_all=True))
#print(cut)

file = open('Text/jielun2.txt','r')
corpus = file.read()
walden = list(jieba.cut(corpus,cut_all=True))
walden = list(jieba.cut(corpus))

#walden = walden.split()
#print(walden)

def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            temp = (arr[i], arr[i + 1])
            pairs.append(temp)
    return pairs


def generate(start_word, num=200):
    start=list(jieba.cut(start_word,cut_all=True))
    print(start)
    if start_word.find("@")==0:
        word=start[-1]
        print(word)
    else:
        word=start[0]
        print(word)

    pairs = makePairs(walden)
    cfd = nltk.ConditionalFreqDist(pairs)
    l = []

    for i in range(num):

        arr = []  # make an array with the words shown by proper count
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)

        l.append(word)
        word = arr[int((len(arr)) * random.random())]
    return ''.join(l)
'''
start='菊花@daney '
song=generate(start)
print(song)
'''