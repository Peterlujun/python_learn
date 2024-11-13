#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 出售金鱼

if __name__ == "__main__":
    flag = 0
    i = 23
    while flag == 0:
        j = 1
        x = i
        while j <= 4 and x >= 11:
            if (x+1)%(j+1) == 0:
                x -= (x+1)/(j+1)
            else:
                x = 0
                break
            j += 1
        if j == 5 and x ==11:                           #循环推出条件  第五次 鱼还剩11条
            print("原来鱼缸中共有%d条金鱼." %i)
            flag = 1
        i += 2                                          #鱼的条数，因为鱼肯定是奇数
