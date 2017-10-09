#!/usr/bin/Python
# -*- coding: utf-8 -*-

#  1：list1,list2,list3 的输出值
def extendlist(val,list = []):
    list.append(val)
    return list
list1 = extendlist(10)
list2 = extendlist(123,[])
list3 = extendlist('a')
print('list1 is {}'.format(list1))
print('list2 is {}'.format(list2))
print('list3 is {}'.format(list3))       #原因：新的默认列表仅仅在函数被定义时创建一次，因此list1和list3操作的是同一个list，而list2操作的是他自己定义的list




