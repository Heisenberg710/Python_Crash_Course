# 列表有一系列按特定顺序排列的元素所组成

language = ['java', 'c', 'c#', 'python', 'php', 'html']
print(language)

# 访问列表元素 ————列表是有序集合，因此要访问列表的任何元素只要将索引告诉python即可

print(language[4].upper())
print(language[-1].upper())  # python访问列表最后一个元素可以直接使用-1的索引

day = ['0', '01', '02', '03', '04', '05', '06', '07']
message = '康复训练第' + day[0] + '天，直接进行一个' + language[-3] + '的训练。'
print(message)

for i in language:
    print(i.upper())

# 修改列表中的元素  包括增删改查

language[0] = 'R语言'  # 知道要修改的元素索引直接进行一个修改
print(language)

language.append('java')  # append增加一个元素直接插入到列表最后一个位置
print(language)

print('')

languages = []
for j in language:
    languages.append(j)
print(languages)

languages.insert(-1, 'javascript')  # .insert方法可以插入元素到任意位置
print(languages)

del language[0]  # 使用del可以删除任何索引的列表元素

for i in languages:
    if i is None:
        print('已经删完咯')
    else:
        del languages[0]
    print(languages)  # 之所以还剩下4个元素是因为上文的for循环

print(language)
print(language + languages)

poped_language = language.pop(-1)
print(language)  # pop也可删除任意索引的元素，与del不同的是pop弹出的元素仍然可以使用
print(poped_language)

print('我学习的第一门编程语言是' + poped_language)

nums = ['0', '1', '1', '2', '3', '1', '2', '1', '0', '0', '2', '1', '2', '1']
for value in nums:
    if '2' in nums:
        nums.remove('2')

print(nums)


# 组织列表--->python提供了许多组织列表的方式可以根据情况使用
# 1、sort()让您能够轻松的对列表进行排序，排列顺序为字母顺序。

language.sort()  # sort()永久性修改排列顺序、无法回到原来的元素排列顺序
print(language)
language.sort(reverse=True)  # 反向操作只需要传参reverse=True给sort()即可
print(language)


# 2、sorted()可以对列表进行临时排序

print('\n原先的language列表顺序：')
print(language)

print('\n使用sorted()之后的列表顺序')
print(sorted(language))
print('\n再打印一次原来的list做对比')
print(language)

num2 = ['18', '1', '17', '12', '10', '26', '23', '22', '39', '37', '38', '46', '35', '2']
num2.sort()  # 此处对数字所组成的list使用sort()进行排序可见是按照第一位数字大小来进行排序
print(sorted(num2, reverse=True))
print(num2)

x = sorted(num2)  # sort()是方法，主要用法是调用  而sorted()则是函数，函数主要进行数据传递、要注意使用方法
print(x)

# 3、使用reverse()可倒着打印列表、对列表操作也是永久性的、但可恢复、只要再执行一次reverse()即可
print('倒着打印之前的list排列顺序：')
print(language)
language.reverse()
print('倒着打印之后的list排列顺序：')
print(language)

# 4、确定列表的长度------>len()

print('\n')
print(len(nums))
print(len(language))  # python计算列表元素顺序时从1开始计算、列表长度不存在差1