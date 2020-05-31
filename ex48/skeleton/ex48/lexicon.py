directions = ('south','north','west','east','center')

""" 
生成dict
列表生成式——循环（if筛选），双层循环，转成大小写（字符串才有这个方法）
字典生成式——直接dict()方法生成
"""
# game_dict = dict(direction = 'south')  # key值为变量，不可为“str”
# game_dict = {"direction" : 'south'}  # key值为“str”，或是int
dire_dict = {v:('directions',v) for v in directions}  

def scan(sentence):
    result = []
    words = sentence.split(" ")#list after split
    for word in words:
        if word in dire_dict.keys():
            t=dire_dict[word]
            result.append(t) 
        # else:
        #     continue
    return result

t=scan('east d north ')
print(t)
"""
1、append()在原list新增，不生成新list，故list.append()返回的是None
2、函数必然有return，若不写，默认为return None
3、split返回的是list
4、若else内容是continu，可不写
5、str.lower()当str本就是小写时，直接返回str
6、(Dictionary) keys() 函数以列表返回一个字典所有的键
"""