#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 分糖果

# 终止条件判断
def judge(candy):
    if candy[0] != candy[1] or candy[1] != candy[2] or candy[2] != candy[3] or candy[4] != candy[3] or candy[4] != candy[5] or candy[5] != candy[6] or candy[7] != candy[8] or candy[8] != candy[9]:
        return 1
    else:
        return 0


def giveSweets(sweet,j):
    t = [0] * 10
    while(judge(sweet)):
        for i in range(0,10):
            if sweet[i] % 2 == 0:
                sweet[i] = sweet[i] // 2
                t[i] = sweet[i]
            else:
                sweet[i] = (sweet[i]+1) // 2
                t[i] = sweet[i] 
        for n in range(0,9):
            sweet[n+1] = sweet[n+1] + t[n]
        sweet[0] = sweet[0]+t[9]
        j += 1
        printResult(sweet,j)

def printResult(s,j):
    print("%4d" %j ,end = " ")
    k = 0
    while k < 10:
        print("%4d" %s[k], end = " ")
        k += 1
        j += 1
    print()

if __name__ == "__main__":
    sweet = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
    print("child 1 2 3 4 5 6 7 8 9 10")
    print("..........................................................")
    print("次数 糖果数")
    j = 0
    print("%4d" %j, end=" ")
    for i in range(len(sweet)):
        print("%4d" % sweet[i], end=" ")
    print()
    giveSweets(sweet,j)