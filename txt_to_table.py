import jieba


def open_file(filename):
    row = open(filename).readlines()
    tokens = []
    for line in row:
        tokens.append(" ".join(jieba.cut(line)))
    return tokens

def txt_to_table(tokens):
    pass

#tokens = open_file('/Users/chenqiutong/Documents/user_speech/face.txt')


import MySQLdb
conn=MySQLdb.connect(host="localhost",user="root",passwd="cqt1234",db="xiaoyuzaijia",charset="utf8")
cursor = conn.cursor()
if conn:
    print("data base has already connected")
with open('/Users/chenqiutong/Documents/user_speech/face.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split('|')
        puffer_id = line[0]
        #print(line)
        for n in range(1,len(line)):
            line[n] = line[n].split(' ')
            face_id = line[n][0]
            sex = line[n][1]
            age = line[n][2]
        #print(line)
        cursor.execute("insert into family(puffer_id,face_id,sex,age) values(%s,%s,%s,%s)",[puffer_id,face_id,sex,age])
cursor.close()
conn.commit()
conn.close()
