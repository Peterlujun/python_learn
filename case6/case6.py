#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 打鱼还是晒网

def runYear(year):
    if (year % 4== 0 and year % 100 != 0) or( year % 400 ==0):
        return 1
    else:
        return 0

def countDay(currentDay):
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    totalday = 0
    year = 1990
    while year < currentDay['year']:
        if runYear(year) == 1:
            totalday = totalday + 366
        else:
            totalday = totalday + 365
        year += 1
    if runYear(currentDay['year']) == 1:
        perMonth[2] += 1
    i = 0
    while i < currentDay['month']:
        totalday += perMonth[i]
        i += 1
    totalday += currentDay['day']
    return totalday

if __name__ == "__main__":
    while True:
        print("Please input 指定日期 包括年，月，日 如：1999 1 31")
        year,month,day = [int(i) for i in input().split()]
        today = {'year':year,'month':month,'day':day}
        
        totalDay = countDay(today)
        print("%d年%d月%d日与1990年1月1日相差 %d 天" % (year, month, day,totalDay))

        # 天数 % 5，判断输出打鱼还是晒网
        result = totalDay % 5
        if result > 0 and result < 4:
            print("今天打鱼")
        else:
            print("今天晒网")