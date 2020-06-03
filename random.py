import random

d = random.sample('abccccc',3)
# random.sample(seq,k)从seq中不重复地取出k个元素，返回列表
t = random.choice('abc')
# random.choice(seq)从seq中取出一个元素
s = random.choices('abc',weights=[1,3,6],k=3)
# random.choices随机选取，可能重复,weight是相对权重
print(d,t,s)

# 对函数定义，如果有默认赋值，则使用时必须重新用=赋值；
# 如果没有默认赋值，则直接填数
