#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 马克思手稿中的数学题

if __name__ == "__main__":
    print("     Men      Women      Children")
    number = 0
    for x in range(0,11):
        y = 20 -2*x
        z = 30 - y - x
        if 3*x + 2*y + z == 50:
            number += 1
            print("%2d:%4d%5d%6d" %(number, x, y, z))