# if语句

games = ['CS GO', 'wow', 'deathStranding']

for game in games:
    if game == 'wow':  # 判断是否相等用'=='
        print(game.upper())

# 检查是否相等

sport = 'football'
if sport == 'FOOTBALL':
    print('yes')
else:
    print('No')  # 此处输出结果为No说明大小写不同不被认同是同一string、转化为小写在进行对比

for game in games:
    if game.lower() == 'cs go':
        print('是cs go了')

# 检查是否不相等

for game in games:
    if game != 'wow':
        print('该游戏不是wow，该游戏是' + game)
    else:
        print('该游戏是wow')

# 比较数字

ages = [15, 31, 22, 18]
for age in ages:
    if age >= 18:
        print('已成年')
    else:
        print('未成年')

# 使用and检查多个条件

i = 17
j = 21
if i > 18 and j > 18:
    print('\n两者都已成年')
else:
    print('\n有未成年混入其中')

# 使用or也能检查多个条件 、只不过只要满足其中任意一个就会返回、两个选项都不满足时返回False

i = 17
j = 12
if i > 18 or j > 18:
    print('\n两者里有成年人')
else:
    print('\n都是未成年')

# 检查特定值是否存在可以选择用in

if 'wow' in games:
    print('\nwow已经在游戏库中')
else:
    games.append('OverWatch')
    print('\nwow不在库中，现已经添加进去')

if 'OverWatch' in games:
    print('\n守望先锋已经在游戏库中')
else:
    games.append('OverWatch')
    print('\nOverWatch不在库中，现已经添加进去')

# if-elif-else结构

age = 4
if age <= 4:
    price = 0
elif 4 < age <= 18:
    price = 25
else:
    price = 50

print('您的票价为：' + str(price) + '元，谢谢参观！')

# 多个elif代码块

age = 31

if age <= 4:
    price = 0
elif 4 < age <= 18:
    price = 5
elif 18 < age < 65:
    price = 10
elif 65 <= age:
    price = 5

print('\n购买票价为：' + str(price) + '元 谢谢参观！')

ob = ['雕哥', '宝哥', '龙神', '胖头', '大狗', '大Mu', '核桃', '谢彬', '马甲', '566']
for player in ob:
    if player == '谢彬':
        print('谢彬是谁？？？')
    elif player == '胖头':
        print('法国士兵！！！')
    else:
        print(player + 'nb!!!')

# 检查列表是否为空

games = []
if games:
    for game in games:
        print('\n圣诞大折扣所要购买的游戏有：')
else:
    print('\n购物车中没有任何游戏、快去添加吧！')

# 使用多个列表

my_games = ['Dota2', 'CS GO', 'WOW', 'Over Watch', 'Death Stranding', 'Cyberpunk2077', 'Dark Dungeon']
fri_games = ['Dota2', 'CS GO', 'WOW', 'lol']

for fri_game in fri_games:
    if fri_game in my_games:
        print('我们共同喜欢的游戏有：' + fri_game.upper())
    else:
        print('我不喜欢玩' + fri_game.upper() + '但是她好像蛮喜欢的')

