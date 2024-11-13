#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 爱因斯坦的数学题

def computing_ladder(n):
    print("在1-%d之间的阶梯数为：" %n)
    sum = 0
    for i in range(7,n+1):
        if (i % 7 == 0) and (i % 6 == 5) and (i % 5 == 4) and (i % 3 == 2):
            sum += 1
            print("%d" %i)
    print("在1-%d之间，有%d个数可以满足爱因斯坦对阶梯的要求。" %(n, sum))

if __name__=="__main__":
    while True:
        n = int(input("请输入n值： "))
        computing_ladder(n)