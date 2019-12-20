# dict储存的"key:value"是无序的，即不可用索引号切片等。del stuff[0]故报错
# dict能将两个物体相关联，不管他们的类型是什么
def new(num_buckets = 256):
    """
    Initializes a Map with the given number of buckets.
    用list创建一个dict aMap=[[],[],[]……]
    为什么要用num_bucket？不直接用256
    """
    aMap = []
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap,key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    # 模除即取余数，故余数不可能大于255.可以用这个方法来限制大数
    # 用new()创建的字典，长度必然都是256，len(aMap)==256
    # 传进来二维列表和key，通过这个函数，把key转换成二维列表内部的index，二维列表是有序的，故存在index
    return hash(key) % len(aMap)

def get_bucket(aMap,key):
    """
    Given a key,find the bucket where it would go.
    找到key在aMap中的bucket_id)
    为啥不跟上一个函数合并？
    返回的是aMap这个二维函数里，以buck_id为索引的元素（也是一个列表）
    """
    bucket_id = hash_key(aMap,key)
    return aMap[bucket_id]

def get_slot(aMap,key,default=None):
    """
    Returns the index,key,and value of a slot found in a bucket.
    Returns -1,key,and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap,key)#bucket是一个列表，是二维列表的第二层，故可迭代
    # i表示key的索引值，k是key本身，v是key的值
    """
    enumerate(squence,[start=0])将一个可遍历对象组合为一个索引序列，同时列出数据和下标
    print(list(enumerate(states))) 
    print(tuple(enumerate(states)))
    """
    # i是enumerate()函数生成的索引，kv是bucket()里的值，可能有多个？？
    for i,kv in enumerate(bucket):
        k,v = kv
        if key  == k:
            return i,k,v

    return -1,key,default

def get(aMap,key,default=None):
    """Gets the value in a bucket for the given key,or the default.
    取出values
    """
    i,k,v = get_slot(aMap,key,default=default)
    return v

def set(aMap,key,value):
    """Sets the key to the value,replacing any exiting value.
    新增或重置一对kv
    """
    bucket = get_bucket(aMap,key)
    i,k,v = get_slot(aMap,key)

    if i >=0:
        # the key exists,replace it
        bucket[i] = (key,value)
    else:
        # the key does not,append to create it
        bucket.append((key,value))

def delete(aMap,key):
    """Deteles the given key from the Map."""
    bucket = get_bucket(aMap,key)

    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map.
    取出k-v
    """

    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print(k,v)

