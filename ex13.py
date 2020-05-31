from sys import argv

script, first = argv

print('This script is called:', script)
print(int(first)+2)     #命令行传入的参数都是str
input('please input your dream:')
print('It is nice.You will realize it')