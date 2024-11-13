#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 换分币

if __name__ == "__main__":
    count = 0
    print("可能的兑换方法如下： ")
    for x in range(0,50+1,10):
        for y in range(0,50-x+1,5):
            for z in range (0,50-x-y+1,1):
                if (x + y + z == 50):
                    count += 1
                    if count %3 == 0:
                        print(count,end= "  ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z))
                    else:
                        print(count, end=" ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z),end=" ")