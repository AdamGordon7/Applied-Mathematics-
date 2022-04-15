from math import *
from numpy import *
from pandas import *
from sympy import *

def newton(f_x,deriv_f,x0):

    n=0
    curr_x=x0

    while(n<=10):
        new_x=curr_x-((f_x(curr_x))/(deriv_f(curr_x)))
        curr_x=new_x 
        n+=1

    return curr_x


deriv_f=lambda x: e**(-x)-(x**2)
f=lambda x: (-e)**(-x)-(2*x)
print(newton(f, deriv_f,1))