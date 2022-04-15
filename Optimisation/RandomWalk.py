import numpy as np
from random import random
from numpy.lib import math
from numpy.random import rand
def random_walk(f, x0, lam, eps, n, N):

    while lam>eps:
        #f1 is func val at f(x0)
        f1=f(x0[0],x0[1])
        i=0
    
        while i<N:
            #generate n random numbers
            rand_num=[]
            rand_num=-1+(rand(n)*(2))
    
            #calc a
            denom=0
            for x in rand_num:
                denom+=x**2

            a=1/np.sqrt(denom)
            
            if a<=1:
                #calc u
                u=a*rand_num
                x=x0+lam*u
                f_val=f(x[0],x[1])
                i+=1
                
                if f_val<f1:
                    x0=x
                    f1=f_val
   
            
            
                
        lam=lam/2

    xOpt=x0
    fopt=f1

    return fopt, xOpt
                


f = lambda x1, x2: x1 - x2 + 2*x1**2 + 2*x1*x2 + x2**2 
x0 = np.array([0, 0])
lam = 1
eps = 0.05
n=2
N = 100
print(random_walk(f, x0, lam, eps, n, N))