# 函数input让程序暂时停止等待用户输入一些文本

name = input('输入自己的名字: ')
print(name + '，你好！')

# 使用int()来获取数值输入

age = input(name + '，输入你的年龄：')
age = int(age)
if age < 18:
    print('未成年🔞')
elif 18 < age < 40:
    print('中年人')
else:
    print('老年人')

# 求模运算符 用来求a/b剩下的余数

a = 5
b = 3
i = 6
c = a % b
print('')
print(c)
if c % 2 == 0:
    print('c是个偶数')
else:
    print('c是奇数')

# 