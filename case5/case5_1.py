#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 借书方案知多少

if __name__ == "__main__":
    i = 0
    print("A,B,C三人所选书号分别为：")
    a = 1
    while a <= 5:
        b = 1
        while b <= 5:
            c = 1
            while c <= 5 and a != b:
                if a != c and b != c:
                    print("A:%2d B:%2d C:%2d   "%(a,b,c), end = "")
                    i += 1
                    if i%4 == 0:
                        print()
                c += 1
            b +=1
        a += 1
    print("共有%d种有效借阅方法" % i)