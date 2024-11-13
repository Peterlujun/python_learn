#!/usr/bin/python3 
# -*- coding: utf-8 -*-  
# @author : Peter 
# @desc: 抓交通肇事犯 

if __name__ == "__main__":
    flag = 0
    for i in range(10):
        if flag == 1:
            break
        for j in range(10):
            if flag == 1:
                break
            if i != j:
                k = 1000 * i + 100 * i  + 10 * j + j
                for temp  in range(31,100):
                    if temp * temp == k:
                        print("车牌号为：",k)
                        flag = 1
                        break