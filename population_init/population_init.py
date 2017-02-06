#!/usr/bin/env python
#encoding:UTF-8
import random

#种群初始化函数
def population_init(population, N, V, minRealVal, maxRealVal):
    del population[:]

    rangeRealVal=[maxRealVal[i]-minRealVal[i] for i in xrange(V)]

    for i in xrange(N):
        tempIndividual=[]
        for j in xrange(V):
            temp=random.uniform(0, 1)*rangeRealVal[j]+minRealVal[j]
            tempIndividual.append(temp)
        population.append(tempIndividual)


#测试代码
if __name__=="__main__":
    population=[]
    N=200
    V=2
    minRealVal=(-5, -5)
    maxRealVal=(5, 5)
    population_init(population, N, V, minRealVal, maxRealVal)
    print population

