import re
from collections import Counter

def count():
    #打开并读取文件
    with open(r'C:\Users\28240\Documents\GitHub\python\jhgdike\0004\test.txt') as file:
        enlish_text = file.read()
        file.close()
    #设置正则表达式并匹配
    wordlimit = r'[a-zA-Z]+'
    words = re.findall(wordlimit,enlish_text)
    #使用counter筛选并计数单词出现频率
    b = Counter(words).items()
    #打印字典
    print(Counter(words).items())
    #用遍历字典value的方法计单词总数
    sum1 = 0
    for k,v in b:
        sum1+=v
    print(sum1)
    #用counter提供的方法获取单词总数
    c = sum(Counter(words).values())
    print('\n'+str(c))
c = count()
#参考资料：http://www.pythoner.com/205.html