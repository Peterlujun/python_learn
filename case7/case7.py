#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 最佳存款方案

if __name__ == "__main__":
    i = 0 
    money = 0.0
    while i < 5:
        money = (money + 1000 ) / (1 + 12 * 0.0063)
        i += 1
    print("应该存入的钱为： %0.2f" %money)