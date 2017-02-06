#!/usr/bin/env python
#encoding:UTF-8
import random

#实数编码,SBX交叉
def crossover(population, pcross_real, V, minRealVal, maxRealVal, eta_c):
    for i in xrange(0, len(population), 2):
        #如果随机概率大于交叉概率则不进行交叉操作
        if random.random()>pcross_real:
            continue

        #对两个个体执行SBX交叉操作 
        for j in xrange(V):
            #对某自变量交叉
            ylow=minRealVal[j]
            yup=maxRealVal[j]
            y1=population[i][j]
            y2=population[i+1][j]
            r=random.random()
            if r<=0.5:
                betaq=(2*r)**(1.0/(eta_c+1.0))
            else:
                betaq=(0.5/(1.0-r))**(1.0/(eta_c+1.0))

            child1=0.5*( (1+betaq)*y1+(1-betaq)*y2 )
            child2=0.5*( (1-betaq)*y1+(1+betaq)*y2 )
            child1=min(max(child1, ylow), yup)
            child2=min(max(child2, ylow), yup)

            population[i][j]=child1
            population[i+1][j]=child2

"""
#实数编码,SBX交叉
def crossover(population, pcross_real, V, minRealVal, maxRealVal, eta_c):
    for i in xrange(0, len(population), 2):
        #如果随机概率大于交叉概率则不进行交叉操作
        if random.random()>pcross_real:
            continue

        #对两个个体执行SBX交叉操作 
        for j in xrange(V):
            #判断是否对某自变量交叉
            if random.random()>0.5:
                continue
            #如果两个体某自变量相等则不操作
            if population[i][j]==population[i+1][j]:
                continue

            #对某自变量交叉
            y1=min(population[i][j], population[i+1][j])
            y2=max(population[i][j], population[i+1][j])
            ylow=minRealVal[j]
            yup=maxRealVal[j]
            r=random.random()

            beta=1.0+(2.0*(y1-ylow)/(y2-y1))
            alpha=2.0-beta**( -(eta_c+1.0) )
            if r<=(1.0/alpha):
                betaq=(r*alpha)**(1.0/(eta_c+1.0))
            else:
                betaq=(1.0/(2.0-r*alpha))**(1.0/(eta_c+1.0))
            child1=0.5*( (y1+y2)-betaq*(y2-y1) )
 
            beta=1.0+(2.0*(yup-y2)/(y2-y1))
            alpha=2.0-beta**( -(eta_c+1.0) )
            if r<=(1.0/alpha):
                betaq=(r*alpha)**(1.0/(eta_c+1.0))
            else:
                betaq=(1.0/(2.0-r*alpha))**(1.0/(eta_c+1.0))
            child2=0.5*( (y1+y2)-betaq*(y2-y1) )
            
            child1=min(max(child1, ylow), yup)
            child2=min(max(child2, ylow), yup)

            population[i][j]=child1
            population[i+1][j]=child2
"""
if __name__=="__main__":
    population=[[1.1, 2.2], [3.3, 4.4], [1.2, 2.3], [3.4, 4.5]] 
    pcross_real=1.0
    V=2
    minRealVal=(-5, -5)
    maxRealVal=(5, 5)
    eta_c=1.0
    crossover(population, pcross_real, V, minRealVal, maxRealVal, eta_c)
    print population
