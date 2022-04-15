

#---------------------------------QUESTION 1:----------------------------------------
import numpy as np 

def Hilbert(n):
    H=np.zeros(shape=(n,n))
    for i in range(0,n,1):
        for j in range (0,n,1):
            H[i][j]=1/((i+1)+(j+1)-1)
    
    return H

H=Hilbert(5)
print(H)





#---------------------------------QUESTION 2:-----------------------------------------

import numpy as np 

def Hilbert(n):
    H=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range (n):
            H[i][j]=1/((i+1)+(j+1)-1)

    return H

def sum_major_diag():
    n=1000
    H=Hilbert(n)
    main_diag=[]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                main_diag.append(H[i][j])

    sum_main=sum(main_diag)

    return sum_main

def sum_upper_diag():

    n=1000
    H=Hilbert(n)
    upper_diag=[]

    for i in range(n):
        for j in range(n):
            if i==j and j!=n-1:
                upper_diag.append(H[i][j+1])
                
    sum_upper_diag=sum(upper_diag)
    return sum_upper_diag

def sum_lower_diag():

    n=1000
    H=Hilbert(n)
    lower_diag=[]

    for i in range(n):
        for j in range(n):
            if i==j and i!=n-1:
                lower_diag.append(H[i+1][j])
                
    
    return sum(lower_diag)


sum_main=sum_major_diag()
sum_upper=sum_upper_diag()
sum_lower=sum_lower_diag()

print("Main diagonal: ", sum_main)
print("Upper diagonal: ", sum_upper)
print("Lower diagonal: ", sum_lower)





#------------------------------------QUESTION 3:--------------------------------------

import numpy as np
def norm_x0(x0):
    denom=0
    u0=[]

    for i in x0:
        denom+=(i**2)

    denom=np.sqrt(denom)

    for i in x0:
        u0.append(i/denom)
    
    u0=np.array(u0)
    
    return u0



def Power_method(A,x0,n):

    eigenvalue=0
    eigenvector=x0
    
    for i in range(n):
        u0=norm_x0(x0)
        u0T= np.transpose([u0])
        
        u0A=np.matmul(u0,A)
        eigenvalue=float(np.matmul(u0A,u0T))
        
        next_x=np.matmul(A,u0)
        x0=next_x

    eigenvector=x0

    return eigenvalue,eigenvector


#example from lecture slides to show working
A=np.array([[1,3],[2,2]])
n=15
x0=[-5,5]
print(Power_method(A,x0,n))




#-------------------------------QUESTION 4:------------------------------------------

import numpy as np
from numpy.lib.index_tricks import _diag_indices_from

def Hilbert(n):
    H=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range (n):
            H[i][j]=1/((i+1)+(j+1)-1)

    return H


def norm_x0(x0):
    denom=0
    u0=[]

    for i in x0:
        denom+=(i**2)

    denom=np.sqrt(denom)

    for i in x0:
        u0.append(i/denom)
    
    u0=np.array(u0)
    
    return u0



def Power_method(A,x0,n):

    eigenvalue=0
    eigenvector=x0
    for i in range(n):
        u0=norm_x0(x0)
        u0T= np.transpose([u0])
        
        u0A=np.matmul(u0,A)
        eigenvalue=float(np.matmul(u0A,u0T))
        
        next_x=np.matmul(A,u0)
        x0=next_x
    eigenvector=x0

    return eigenvalue,eigenvector
    
def dom_eigval_H(x0,n):
    H=Hilbert(123)

    dom_eigens=Power_method(H,x0,10)
    dom_eigen_val=dom_eigens[0]
    dom_eigen_vec=dom_eigens[1]

    return dom_eigen_val, dom_eigen_vec


n=10
x0=[]
for i in range(123):
    x0.append(1)

eig_val=dom_eigval_H(x0,n)[0]
print(eig_val)




#----------------------------------QUESTION 5----------------------------------------

from operator import ne
import sympy as sym
import numpy as np
from sympy.core.symbol import symbols
from sympy.utilities.lambdify import lambdify

def jacobian(J,x0):
    J=J(x0)

    return J

def calc_next_x(J_inv, F, x0):

    J_invxF=np.matmul(J_inv,F)
    next_x=np.subtract(x0, J_invxF)

    return next_x


def Newton(F, J, x0, tol):

    curr_x=x0

    while(True):
        J_curr=jacobian(J,curr_x)

        J_inv=np.linalg.inv(J_curr)
        F_curr=F(curr_x)

        next_x= calc_next_x(J_inv, F_curr, curr_x)

        stop_val=(np.linalg.norm(next_x-curr_x))/(np.linalg.norm(curr_x))
        if(stop_val<tol):
            break

        curr_x=next_x
       

    return curr_x


x0=np.array([-0.6,0.6])
F= lambda x: np.array([(x[0]**3)-(3*x[0]*(x[1]**2))-1, (3*(x[0]**2)*x[1])-(x[1]**3)])
J= lambda x: np.array([[3*x[0]**2 -3*x[1]**2, -6*x[0]*x[1]], 
                      [6*x[0]*x[1], 3*x[0]**2 - 3*x[1]**2]])


print(Newton(F,J,x0,1e-6))




#----------------------------------QUESTION 6:--------------------------------------

from operator import ne
import sympy as sym
import numpy as np
from sympy.core.symbol import symbols
from sympy.utilities.lambdify import lambdify

def jacobian(J,x0):
    J=J(x0)

    return J

def calc_next_x(J_inv, F, x0):

    J_invxF=np.matmul(J_inv,F)
    next_x=np.subtract(x0, J_invxF)

    return next_x


def Newton(F, J, x0, tol):

    curr_x=x0

    while(True):
        J_curr=jacobian(J,curr_x)

        J_inv=np.linalg.inv(J_curr)
        F_curr=F(curr_x)

        next_x= calc_next_x(J_inv, F_curr, curr_x)

        stop_val=(np.linalg.norm(next_x-curr_x))/(np.linalg.norm(curr_x))
        if(stop_val<tol):
            break

        curr_x=next_x
       

    return curr_x

#make y y'?
y_prime=lambda y,i: (y[i+1]-y[i-1])/2*(1/3)
f=lambda x,y: 1/8*((32+(2*x**3)-(y*y_prime)))

F=lambda y:np.array([-((y[2]-2*(17)+y[0])/(1/3)**2), -(((43/3)-2*y[2]+17)/(1/3)**2),
                    -((y[4]-2*(43/3)+y[2])/(1/3)**2),-((y[5]-2*y[4]+(43/3))/(1/3)**2),
                    -((y[6]-2*y[5]+y[4])/(1/3)**2)])

J=lambda y: np.array([])
y1=17
y3=43/3

yy0=[17,17,17,17,17]



#----------------------------------QUESTION 7:--------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5,6])
y=np.array([0,1,2,3,4,5,6])

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("LINE PLOT OF X AGAINST Y")
plt.plot(x,y)
plt.show()