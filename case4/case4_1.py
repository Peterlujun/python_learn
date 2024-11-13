#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author :   Peter
# @desc: 百钱百鸡问题

if __name__ == "__main__":
    cock = 0
    while cock <= 20:
        hen = 0
        while hen <= 33:
            chicken = 100 - cock - hen
            if 5 * cock + 3 * hen + chicken /3.0 == 100:
                print("cock = %2d,hen = %2d,chicken = %2d"%(cock,hen,chicken))
            hen += 1
        cock += 1