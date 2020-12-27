message = "🔪🐘"
print(message)
#  此处 message 是个变量，每个变量都会存储一个值————与变量相关联的信息

message = '🔪🐘🔪🐘🔪🐘'
print(message)
#  在程序中可以随时修改变量的值，python始终记录变量最新的值

print(message)  # 注释距离代码起码空两行

print('asdf', end='\n')  # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) print的原型

# 字符串就是一系列字符、不论是被单引号还是双引号扩起来的都是字符串
str1: str = 'this is a string'

str2 = "and this is also a string"

print(str1)
print(str2)

str3 = '123456789'
for i in str3:
    print(i),

name = 'walter white'
print(name.title())

# 合并、拼接字符串

first_name = 'white'
last_name = 'walter'
fullname = last_name.title() + ' ' + first_name.title()
print(fullname)

message = 'Hello ' + fullname + ",today is Friday！Don't warry,be happy!"
print(message)

#  使用制表符来进行换行或是添加空白
print('asdfghjkl')
print('\tasdfghjkl')  # \t

print('asdfghjkl')
print('a\ns\nd\nf\ng\nh\nj\nk\nl\n\n')  # \n

print('Languages:\n\tPython\n\tC\n\tJava\n\tC#\n\tSwift\n')  # \n\t

i = 9
j = 7

print(i/j)

#  python将带有小数点的全部称为浮点数

i = 0.4
j = 0.9
print(i/j)

age = 23
message = "\nHappy " + str(age) + "rd birthday!"  # 此处需要将age这个变量强转为str类型
print(message)