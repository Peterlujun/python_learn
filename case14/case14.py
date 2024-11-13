'''
列表是以方括号“[]”包围的数据集合，列表元素之间使用逗
号“,”分割。列表的元素类型可以是任何数据类型，也可以包含另
一个列表，可以通过列表的下标来访问列表中的元素，下标从0开
始。列表的内容是可变的，
'''

'''
Python的元组与列表相似，元组是以圆括号“()”包围的数据
集合。与列表不同的是元组的元素一旦确定就不能再改变，它是不
可变数据类型。因此它常常被用在不希望数据被其他操作所改变的
场景中
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 个人所得税问题

TAXBASE = 2000
#分为9个阶段，每个阶段第一个值为个税起征点，第二个值为该阶段截止点，第三个值为税率
TaxTable = [(0, 500, 0.05),
            (500, 2000, 0.10),
            (2000, 5000, 0.15),
            (5000, 20000, 0.20),
            (20000, 40000, 0.25),
            (40000, 60000, 0.30),
            (60000, 80000, 0.35),
            (80000, 100000, 0.40),
            (100000, 1e10, 0.45)]
#计算税收
def CaculateTax(profit):
    tax = 0.0
    profit -= TAXBASE                                   # 超过个税起征点的收入
    i = 0
    for i in range(len(TaxTable)):
        if (profit > TaxTable[i][0]):
            if (profit > TaxTable[i][1]):               # profit超过当前的缴税范围
                tax += (TaxTable[i][1] - TaxTable[i][0]) * TaxTable[i][2]
            else:                                       # profit未超过当前的缴税范围
                tax += (profit - TaxTable[i][0]) * TaxTable[i][2]
            profit -= TaxTable[i][1]
            if profit < 0:
                profit = 0
            print("征税范围：%6d～%6d 该范围内缴税金额：%6.2f 超出该范围的金额：%6d" 
                  %(TaxTable[i][0], TaxTable[i][1], tax, profit))
    return tax

if __name__ == '__main__':
    print("请输入个人收入金额: ", end='')
    profit = int(input())
    tax = CaculateTax(profit)
    print("您的个人所得税为 %12.2f" % tax)