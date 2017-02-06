#!/usr/bin/env python
#encoding:UTF-8
import random
#Routine for real polynomial mutation of an individual
#实数编码的常规多项式变异

def mutation(population, pmut_real, V, minRealVal, maxRealVal, eta_m):
    for i in xrange(len(population)):
        for j in xrange(V):
            r=random.random()
            #对个体某变量进行变异
            if r<=pmut_real:
                y=population[i][j]
                ylow=minRealVal[j]
                yup=maxRealVal[j]
                delta1=1.0*(y-ylow)/(yup-ylow)
                delta2=1.0*(yup-y)/(yup-ylow)
                #delta=min(delta1, delta2)
                r=random.random()
                mut_pow=1.0/(eta_m+1.0)
                if r<=0.5:
                    xy=1.0-delta1
                    val=2.0*r+(1.0-2.0*r)*(xy**(eta_m+1.0))
                    deltaq=val**mut_pow-1.0
                else:
                    xy=1.0-delta2
                    val=2.0*(1.0-r)+2.0*(r-0.5)*(xy**(eta_m+1.0))
                    deltaq=1.0-val**mut_pow
                y=y+deltaq*(yup-ylow)
                y=min(yup, max(y, ylow))
                population[i][j]=y


