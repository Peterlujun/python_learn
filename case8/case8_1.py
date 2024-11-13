#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 选择排序

def selectionSort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[j] < a[i]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    for i in a:
        print(i,end= " ")
if __name__ == "__main__":
    print("请为列表元素赋初值，列表末尾不能有空格：")
    x = input()
    x = x.split()
    for i in range(0,len(x)):
        x[i] = int(x[i])
    print("你输入的列表元素为：")
    print("经过交换后的数组元素为：")
    selectionSort(x)