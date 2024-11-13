#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 亲密数

if __name__ == "__main__":
    print("3000以内的全部亲密数为：")
    for a in range(1,3000):
        b = 0
        i =1
        while i <= (a//2):
            if a % i == 0:
                b += i
            i += 1
        n = 0
        j = 1 
        while j <= (b//2):
            if b % j == 0:
                n = n + j
            j += 1
        if n == a and a > b :          #避免重复输出
            print("%4d -- %4d \t" %(a, b))