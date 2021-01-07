# for循环用于针对集合内每个元素的代码块 而while循环执行直到条件不满足为止

current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

# 使用while可让用户自己选择在何时进行退出

sher = '\n华生，随意输入一些你想输入的东西：'
sher += "\n输入'exit'来退出该程序\n"
message = ''
while message != 'exit':
    message = input(sher)
    print(message)

# 使用标志

sher = '\n华生，随意输入一些你想输入的东西：'
sher += "\n输入'exit'来退出该程序\n"

active = True
while active:
    message = input(sher)

    if message == 'exit':
        print('盲生，你发现了华点！！')
        active = False
    else:
        print('盲生，你还没有发现华点吗')

# 使用break退出循环

sher = '\n华生，随意输入一些你想输入的东西：'
sher += "\n输入'exit'来退出该程序\n"

while True:
    sherlock = input(sher)
    if sherlock == 'exit':
        print('盲生，你发现了华点！！')
        break
    else:
        print('盲生，你还没有发现华点吗')

# 