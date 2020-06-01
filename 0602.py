#过滤列表在的负数
result = [i for i in data if i >=0]     #列表推导式
result = fliter(lambda x: x>=0, data)

#筛选字典的value，并返回key。筛选分数超过80的学生
d = {x: randint(50,100) for x in range(1,21)}
{k: v for k, v in d.items() if v>= 80}