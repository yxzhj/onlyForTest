with open('workfile.txt','r+') as f:
    # f.write('123')
    # f.seek(4)
    t = f.read()
    print(t)
    a = f.seek(3)
    print(a)
    print(t[a])




'''

seek()返回偏移的光标位置,seek(3)从前往后数第3位；
whence默认为0时，offset不能为负，因为光标在文件开始时，再往前没有数据了
seek(-3,2)从后往前数3位
offset为正，则从前往后数，为负则从后往前数
当offset大于文件内容的长度时，光标移动了，但是后面的内容为空
offset和whence同为正，基本读取都是空的

'''