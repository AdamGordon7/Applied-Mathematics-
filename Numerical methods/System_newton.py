from math import *
from mpmath.calculus.optimization import jacobian
from numpy import *
from pandas import *
from sympy import *



def jacob(x0, y0):
    x=Symbol('x')
    y=Symbol('y')

    f=(x**3)-(3*x*(y**2))-1
    f_prime_x=f.diff(x)
    f_prime_y=f.diff(y)

    f=lambdify([x,y],f)
    f_prime_x=lambdify([x,y],f_prime_x)
    f_prime_y=lambdify([x,y],f_prime_y)
    print(f_prime_x)
    print(f_prime_y)

    g=(3*(x**2)*y)-(y**3)
    g_prime_x=g.diff(x)
    g_prime_y=g.diff(y)

    g=lambdify([x,y],g)
    g_prime_x=lambdify([x,y],g_prime_x)
    g_prime_y=lambdify([x,y],g_prime_y)

    
    fx=f_prime_x(-0.6,0.6)
    fy=f_prime_y(-0.6,0.6)
    gx=g_prime_x(-0.6,0.6)
    gy=g_prime_y(-0.6,0.6)

    arr=create_matrix(fx,fy,gx,gy)

   # jacob_arr.linalg.inv()

    return

def create_matrix(fx,fy,gx,gy):
    jacob_arr=array[[fx,fy], [gx,gy]]
    return jacob_arr






jacob(-0.6,0.6)



