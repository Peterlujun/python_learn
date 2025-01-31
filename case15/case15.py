#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : Peter
# @desc: 存钱问题

if __name__ == "__main__":
    max = 0.0
    for x8 in range(0,3):
        t5 = (20 - 8*x8)//5
        for x5 in range(0,t5 + 1):
            t3 = (20 -8*x8 - 5*x5)//3
            for x3 in range(0,t3+1):
                t2 = (20 -8*x8 - 5*x5 - 3 *x3)// 2
                for x2 in range(0,t2+1):
                    x1 = 20-8*x8-5*x5-3*x3-2*x2
                    result = 2000* ((1+0.0063*12)**x1) * ((1+2*0.0066*12)**x2)* ((1+3*0.0069*12)**x3) * ((1+5*0.0075*12)**x5) * ((1+8*0.0084*12)**x8)
                    if result > max:
                        max = result
                        y1 = x1
                        y2 = x2
                        y3 = x3
                        y5 = x5
                        y8 = x8
    print("获得利息最多的存款方式为：");
    print("8年期限的存了%d次" %y8);
    print("5年期限的存了%d次" %y5);
    print("3年期限的存了%d次" %y3);
    print("2年期限的存了%d次" %y2);
    print("1年期限的存了%d次" %y1);
    print("存款人最终的获得的本利合计：%0.2f" %result)