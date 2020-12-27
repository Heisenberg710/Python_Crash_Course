import time
# 1、遍历整个列表

ob = ['Zhou', '宝哥', '阿龙', '胖头', '大狗', '大Mu', '核桃', '？？', '马甲', '566']
for new_ob in ob:
    print(new_ob)

for new_ob in ob:
    if new_ob is '胖头':
        print('胖头鱼受死！！！')
    else:
        print(new_ob + ':湖南帮成立就在今天！！！')
        print(new_ob + ':干特么的胖头鱼！！！\n')


# 2、创建数值列表————使用range()

for value in range(0, 11):
    print(value)

# 3、要创建数字列表可使用函数list()将range()的结果直接转换成列表

number = list(range(1, 6))  # range()可作为list的参数
print(number)

numbers = list(range(0, 1024, 10))
print(numbers)

# 使用零时变量的一种表达

num = []
for value in range(1, 11):  # **表乘方
    number = value ** 2
    num.append(number)

print('\n')
print(num)

# 不使用零时变量的一种表达

num1 = []
for value_1 in range(1, 11):
    num1.append(value_1 ** 2)
print(num1)

# 对数字列表进行简单的计算
print('\n')

print(max(num1))  # 求列表中最大的数

print(min(num1))  # 求列表中最小的数

print(sum(num1))  # 求列表中的数的和

# 对列表进行解析  可以只使用一行代码就实现从创建列表到赋值

num1 = [value ** 3 for value in range(1, 11)]
print(num1)

# 练习题

# 1、使用一个for循环打印数字1-20（含）

num1 = [value for value in range(1, 21)]
print(num1)

# 2、创建一个列表，其中包含数字1-1 000 000

million = [value for value in range(1, 1000001)]
print(million)

# 3、使用上个million列表 使用min（）与max（）确保是从1开始到1000000结束并调用sum（）测试需要多久时间能处理完

print(min(million))
print(max(million))

start = time.time()  # 求时间需要import time 标记开始测试时间
print(sum(million))
end = time.time()  # 标记结束时间
print('sum求和共用了' + str(end-start) + '秒')

# 4、通过给函数range（）指定第三个参数来创建一个列表，其中包含1-20的奇数，再使用一个for循环将他们打印出来

num1 = [value for value in range(1, 20, 2)]
for i in num1:
    print(i)

# 5、创建一个列表，将3-30中能被3整除的数加进去，再使用一个for循环将他们打印出来

num1 = [value for value in range(3, 31, 3)]
print(num1)

for value in num1:
    print('能被3整除的数：' + str(value))


# 使用列表的一部分
# 1、切片  要使用切片需指定切片的第一个索引与最后一个索引

print(ob)
print(ob[0:3])
print(ob[:5])  # 如果没有指定第一个索引，则默认从第一个元素开始直到终止索引
print(ob[4:])  # 如果要让切片终止与最后一个元素则可省略终止索引
print(ob[-4:])  # 负数索引取倒数n位

# 2、遍历切片  遍历切片的作用在于可以将玩家所得分数排序然后制作高分榜

print('ob的成员有：')
for players in ob[0: 10]:
    if players is '？？':
        print('')
    else:
        print(players)

# 复制列表

my_games = ['Dota2', 'CS GO', 'WOW', 'Over Watch', 'Death Stranding', 'Cyberpunk2077', 'Dark Dungeon']
friend_game = my_games[:]
my_games.append('Duet')
friend_game.append('TitanFall2')
print('\n我平时玩的游戏有：')
for mygame in my_games:
    print(mygame)
print('\n朋友平时玩的游戏有：')
for fri_game in friend_game:
    print(fri_game)


my_games1 = ['Dota2', 'CS GO', 'Over Watch', 'Death Stranding', 'Cyberpunk2077', 'Dark Dungeon']
friend_game1 = my_games1  # ！！！如果不使用切片的方式去将一个列表的值赋值给另一个列表会出现两个变量指向同一个列表的情况、更会出现数据错误
my_games1.append('Duet')
friend_game1.append('TitanFall2')
print('\n我平时玩的游戏有：')
for mygame in my_games1:
    print(mygame)
print('\n朋友平时玩的游戏有：')
for fri_game in friend_game1:
    print(fri_game)

# 元组  列表是可以被修改的，而python将不可变的列表称为元组

games = ('Dota2', 'CS GO', 'Over Watch', 'Death Stranding', 'Cyberpunk2077', 'Dark Dungeon')  # 元组使用圆括号而不是方括号
print('\n元组列表数据截取：')
print(games[0])
print(games[1])

# 遍历元组中所有的值可以像遍历列表一样

print('\n我平时玩的游戏有：')
for game in games:
    print(game)

# 修改元组变量 虽然不能修改元组的元素，但是可以给存储元组的变量赋值，通过重新定义整个元组

list1 = ('1', '2', '3', '4', '5')
print(list1)

list1 = ('6', '7', '8', '9', '10')
print(list1)
