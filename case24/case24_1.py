#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 阿姆斯特朗数

if __name__ == "__main__":
    a = [0, 0, 0]
    print("1000以内的阿姆斯特朗数：")
    for i in range(2, 1000):
        t = 0
        k = 1000
        while k >= 10:
            a[t] = (i % k) // (k // 10)
            k = k // 10
            t += 1
        sum = a[0]**3 + a[1]**3 + a[2]**3
        if i == sum:
             print("%d \t" %i, end=" ")