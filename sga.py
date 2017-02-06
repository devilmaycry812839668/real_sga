#!/usr/bin/env python
#encoding:UTF-8
import random
from population_init.population_init import population_init
from function.eval_fun import eval_fun
from selection.selection import selection
from crossover.crossover import crossover
from mutation.mutation import mutation

N=200
V=2
minRealVal=(-5, -5)
maxRealVal=(5, 5)
population=[]
pcross_real=0.9
pmut_real=0.01
eta_c=1
eta_m=1

#目标函数值列表
xReal=[]

def per_run():
    population_init(population, N, V, minRealVal, maxRealVal)

    for i in xrange(200):
        eval_fun(population, xReal)

        selection(population, xReal)
        crossover(population, pcross_real, V, minRealVal, maxRealVal, eta_c)
        mutation(population, pmut_real, V, minRealVal, maxRealVal, eta_m)

    eval_fun(population, xReal)
    return 100.0-max(xReal)

if __name__=="__main__":
    score_list=[]
    for i in xrange(100):
        temp=per_run()
        score_list.append(temp)
        print i, " : ", temp
    print sum(score_list)/len(score_list)

