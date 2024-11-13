#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 水仙花数

if __name__ == "__main__":
    print("result is: ")
    for n in range(100, 1000):
        hun = n // 100
        ten = (n - hun * 100)//10
        ind = n % 10
        m = hun*hun*hun + ten*ten*ten + ind*ind*ind
        if n == m:
            print("%d \t" %n, end=" ")