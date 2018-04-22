import jieba
import re
import codecs
from collections import Counter
import jieba.analyse

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 导入自定义词典
jieba.load_userdict('/Users/chenqiutong/Documents/user_dict.txt')

# 读取文件并分词
def read_file(filename):
    user_speech = open(filename).readlines()
    speech = []
    for line in user_speech:
        speech.append(' '.join(jieba.cut(line)))
    return speech

# 使用正则匹配提取文本中的文字
def reChinese(speech):
    reChinese = re.compile('[\u4e00-\u9fa5]+')
    #user_speech = []
    for i in range(len(speech)):
        teststr = str(speech[i])
        speech[i] = reChinese.findall(teststr)
    return speech

# jieba分词器通过词频获取关键词
def jieba_keywords(speech):

    stopwords = stopwordslist(filepath="/Users/chenqiutong/Documents/stopwords.txt")
    #print(stopwords)
    # 先进行分词，再将分词后的词语与停用词表比较，若是停用词，就将其remove
    corpus = []
    for speech_i in speech:
        #print(speech_i)
        x = []
        x = ' '.join(jieba.cut(str(speech_i)))
        #corpus.append(' '.join(jieba.cut(str(speech_i))))
        #print("去停用词前：",x)
        y= ''
        for word in x:
            if word not in stopwords:
                    y +=word

        #print("去停用词后：",y)
        corpus.append(y)
    # jieba分词器通过词频获取关键字（目前问题：怎么把停用词去掉）
    keywords = jieba.analyse.extract_tags(str(corpus), topK=20)
    #sorted(keywords)
    #print(corpus)
    print(sorted(keywords,reverse=True))


# 载入停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in codecs.open(filepath, 'r', encoding='UTF-8').readlines()]
    return stopwords

"""
def tfidf_keywords(filename):
    corpus = []
    for line in open(filename, 'r').readlines():
        corpus.append(line)

    # 01、构建词频矩阵，将文本中的词语转换成词频矩阵
    vectorizer = CountVectorizer()
    # a[i][j]:表示j词在第i个文本中的词频
    X = vectorizer.fit_transform(corpus)
    #print(X)  # 词频矩阵

    # 02、构建TFIDF权值
    transformer = TfidfTransformer()
    # 计算tfidf值
    tfidf = transformer.fit_transform(X)

    # 03、获取词袋模型中的关键词
    word = vectorizer.get_feature_names()

    # tfidf矩阵
    weight = tfidf.toarray()

    # 打印特征文本
    print(len(word))
    for j in range(len(word)):
        print(word[j])

        # 打印权重
        for i in range(len(weight)):
            for j in range(len(word)):
                print(weight[i][j])
                # print '\n'
"""

