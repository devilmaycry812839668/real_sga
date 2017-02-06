#!/usr/bin/env python
#encoding:UTF-8

#对偶问题， 转化为求最大值
#二维　Rastrigin测试函数
def object_fun(p):
    import math
    x=p[0]
    y=p[1]
    object_value=20.0+x**2+y**2-10.0*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))
    return 100.0-object_value

"""
#求最大值,无需转化
#二维　Schaffer测试函数
def object_fun(p):
    import math
    x=p[0]
    y=p[1]

    object_value =0.5-((math.sin( math.sqrt(x**2+y**2) ))**2-0.5)/(1+0.001*(x**2+y**2))**2
    return object_value
"""
