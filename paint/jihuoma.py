import uuid
import random
st= 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*'
for i in range(0,200):
    '''
    方法一
    运用uuid4
    生成更为复杂，相同率更低的标识码
    '''
#使用uuid4生成识别码，取前10位与st字符串组合
    x=str(uuid.uuid4().fields[-1])[:10]+st
    y=''
    for j in range(0,10):
         y += random.choice(x)
    print (y+"\n")
# for i in range(0,200):
#     '''方法二，简单的随机字符串'''
#     sum = ''
#     for j in range(0,10):
#         d = random.choice(st)
#         sum += d
#     print(sum)