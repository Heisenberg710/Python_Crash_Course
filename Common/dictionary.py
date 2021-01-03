# 字典是一系列key-value 的键值对，可以将数字、字符串、列表甚至字典存储在与键相对应的value中

user_info = {'user_name': 'coco', 'pwd': '123456'}
print(user_info['user_name'])
print(user_info['pwd'])

alien_0 = {'color': 'green', 'points': '10'}
new_points = alien_0['points']
print('\n你击杀了外星人，恭喜你获得' + str(new_points) + '点分数')

# 字典是一种动态结构，可以随时添加键值对

alien_0['x_position'] = 0
alien_0['y_position'] = 10

print(alien_0)

# 先创建一个空字典，之后在进行添加键值对、这在生成大量的key-value时非常实用

game = {}
pass
game['WOW'] = '魔兽世界'
game['DeathStranding'] = '死亡搁浅'
game['OverWatch'] = '守望先锋'

print(game)
game['WOW'] = '魔兽世界'
# 修改字典中的值

alien_0['color'] = 'red'
print(alien_0)

alien_0['speed'] = 'slow'
print('\n外星人移动前所在的坐标为(' + str(alien_0['x_position']) + ',' + str(alien_0['y_position']) + ')')

if alien_0['speed'] == 'slow':
    alien_0['x_position'] = 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] = 2
else:
    alien_0['x_position'] = 3

print('\n外星人移动之后所在的坐标为(' + str(alien_0['x_position']) + ',' + str(alien_0['y_position']) + ')')

# 删除键值对、对于不再需要的信息可实用del将其对应的键值对一起删除

print(game)
del game['WOW']

# 有类似对象组成的字典
ob = {
    '黄翔': 'LongDD',
    '谢彬': '？？？',
    '陈尧': 'Zhou',
    '姜岑': '胖头',
    '陈志豪': 'Hao',
}
print(ob)

# 遍历字典------->1、遍历所有的键值对

for key, value in ob.items():  # .items()
    print('\nKey:' + key)
    print('\nvalue:' + value)

for key, value in ob.items():
    print(key)

# 遍历字典------->2、遍历所有的键  在不需要value时，使用方法key（）可以直接获取key

for ob_name in ob.keys():
    print(ob_name)

# 按顺序遍历字典中的所有键

for ob_name in sorted(ob.keys()):
    print(ob_name)

# 遍历字典中的所有值

for ob_name in ob.values():
    print(ob_name)

# 调用集合set（）可让python找出列表中独一无的没有重复的元素，并用这些元素创建一个集合

ob = {
    '黄翔': 'LongDD',
    '谢彬': '？？？',
    '陈尧': 'Zhou',
    '姜岑': '胖头',
    '陈志豪': 'Hao',
    '1': 'LongDD',
    '2': '？？？',
    '3': 'Zhou',
    '4': '胖头',
    '5': 'Hao',
}
print('\n')
for ob_name in ob.values():
    print(ob_name)
print('\n')
for ob_name in set(ob.values()):
    print(ob_name)

# 将一系列字典存储在列表中 或是将一系列列表作为值存储在字典中 这称为嵌套

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red ', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]
print('')
for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print('')

for alien in aliens[:10]:
    print(alien)

print('总共创建了' + str(len(aliens)) + '个外星人')

for alien in aliens[:30]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print('')

for alien in aliens:
    print(alien)

# 将列表存储在字典中
favorite_heroes = {
    '黄翔': ['墨客', '花仙子', '萨尔'],
    '胖头': ['黑贤', '兔子', 'ds'],
    '雕哥': ['骷髅王', 'TB', '小娜迦'],
    '外人': ['？', '？？', '？？？'],
    '宝哥': ['拉野']
}

for name, heroes in favorite_heroes.items():
    if len(heroes) == 1:
        print('\n' + name + '只有一个绝活就是：' + str(heroes))
    else:
        print('\n' + name + '的绝活英雄是：')
        for hero in heroes:
            print(hero)

# 在字典中存储字典

ACG = {
    '命运石之门': {
        '简介': '《命运石之门》原名：Steins;Gate,故事讲述了一群学生研究和开发可以改变过去的科技。',
        'URL': 'https://v.qq.com/detail/g/gu5m5d0ccelhqw9.html',
        '集数': 25
    },
    'fate/zero': {
        '简介': '作为Fate/stay night的前传，Fate/Zero的故事舞台设定在第五次圣杯战争的10年前，即第四次圣杯战争',
        'URL': 'https://www.bilibili.com/bangumi/play/ep29919?from=search&seid=3510966273635927501',
        '集数': 25
    }
}
print('\n我喜欢的动漫有：')
for ACG_name, ACG_info in ACG.items():
    if ACG_name == '命运石之门':
        print(ACG_name + '的主要剧情是：' + ACG_info['简介'])
        print(ACG_name + '的观看地址是：' + ACG_info['URL'])
    else:
        print(ACG_name + '的主要剧情是：' + ACG_info['简介'])
        print(ACG_name + '的观看地址是：' + ACG_info['URL'])