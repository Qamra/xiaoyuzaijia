import user_speech

user_speech_l = user_speech.read_file('/Users/chenqiutong/Documents/user_speech/baidu_rawtext_20180412-20180412.txt')
user_speech_2 = user_speech.read_file('/Users/chenqiutong/Documents/user_speech/baidu_rawtext_20180407.txt')
#print(user_speech_l)
user_speech_l = user_speech.reChinese(user_speech_l)
user_speech_2 = user_speech.reChinese(user_speech_2)
#print(user_speech_l)
user_speech.jieba_keywords(user_speech_l)
user_speech.jieba_keywords(user_speech_2)
#print(user_speech_l)