#coding:utf-8

# 定义一个列表来模拟栈
stack = []


# 进栈,调用列表的append()函数加到列表的末尾,strip()没有参数是去掉首尾的空格
def pushit():
    stack.append(raw_input('Enter new string: ').strip())


# 出栈,用到了pop()函数
def popit():
    if len(stack) == 0:
        print
        'Cannot pop from an empty stack!'
    else:
        print
        'Removed [', stack.pop(), ']'


# 编历栈
def viewstack():
    print
    stack


# CMDs是字典的使用
CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


# pr为提示字符
def showmenu():
    pr = """ 
  p(U)sh 
  p(O)p 
  (V)iew 
  (Q)uit 
    Enter choice: """

    while True:
        while True:
            try:
                # 先用strip()去掉空格,再把第一个字符转换成小写的
                choice = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print('\nYou picked: [%s]' % choice)

            if choice not in 'uovq':
                print('Invalid option, try again')

            else:
                break

                # CMDs[]根据输入的choice从字典中对应相应的value,比如说输入u,从字典中得到value为pushit,执行pushit()进栈操作
        if choice == 'q':
            break
        CMDs[choice]()

        # 判断是否是从本文件进入,而不是被调用


if __name__ == '__main__':
    showmenu()








