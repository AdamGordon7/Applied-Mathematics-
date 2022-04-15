import numpy as np
from random import random
from numpy.lib import math
from numpy.random import rand
def random_walk(f, x0, lam, eps, n, N):

    funcValF1=f(x0[0],x0[1])
    i=0

    #random set of numbers of size n
    rand_num=[]
    rand_num=-1+(rand(n)*(2))
    
    #calc a
    denom=0
    for i in rand_num:
        denom+=i**2
    a=1/np.sqrt(denom)
    
    if a<=1:
        u=a*rand_num

        #new vec and correspoinfing func val
        x=x0+lam*u
        funcVal=f(x[0],x[1])

        if(funcVal<funcValF1):
            x0=x
            funcValF1=funcVal
            i=0

        if i<=N:
            i=i+1
        
        lam=lam/2
        if lam<=eps:
            xOpt=x0
            fOpt=funcValF1
            return xOpt, fOpt

                


f = lambda x1, x2: x1 - x2 + 2*x1**2 + 2*x1*x2 + x2**2 
x0 = np.array([0, 0])
lam = 1
eps = 0.05
n=2
N = 100
print(random_walk(f, x0, lam, eps, n, N))