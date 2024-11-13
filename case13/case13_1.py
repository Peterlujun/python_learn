#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 求车速

if __name__ == "__main__":
    a = [0,0,0,0,0]
    i = 95860
    while i:
        t = 0
        k = 100000
        while k >= 10:              # 分解5位数并保存
            a[t] = (i%k)//(k// 10)
            k /= 10
            t += 1
        if a[0] == a[4] and a[1] == a[3]:
            print("里程表上出现的新的对称数为：%d%d%d%d%d"%(a[0],a[1],a[2],a[3],a[4]))
            print("该车的速度为%.2f"%((i-95859)/2.0))
            break
        i += 1
