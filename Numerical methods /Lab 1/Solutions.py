#Question 1:
from math import *
from numpy import *

def trapezoidal_rule(f,n,a,b):
    h=(b-a)/n 
    
   
    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*((b-a)/n))
        xvals.append(xi)

    inner_xvals=[]
    for i in range (1,n):
        inner_xvals.append(f(xvals[i]))

    summ=0
    for i in inner_xvals:
        summ+=i

    integral_approx=(h/2)*((f(xvals[0]))+(2*summ)+f(xvals[-1]))


    return integral_approx


f = lambda x: 1 / (1 + x ** 2)
integral=trapezoidal_rule(f,6,0,1)
print(integral)





#Question 2:
def simpson_rule(f,n,a,b):

    h=(b-a)/n
    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*h)
        xvals.append(xi)

    inner4=[]
    for i in range(1,n,2):
        inner4.append(f(xvals[i]))

    sum_inner4=4*(sum(inner4))

    inner2=[]
    for i in range(2,n-1,2):
        inner2.append(f(xvals[i]))

    sum_inner2=2*(sum(inner2))

    integral_approx=(h/3)*(f(xvals[0]) + sum_inner4 + sum_inner2+ f(xvals[-1]))

    return integral_approx

f = lambda x: 1 / (1 + x ** 2)
integral=simpson_rule(f,6,0,1)
print(integral )






#Question 3:
from math import *
from numpy import *

def trapezoidal_rule(f,n,a,b):
    h=(b-a)/n 
    
    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*((b-a)/n))
        xvals.append(xi)

    inner_xvals=[]
    for i in range (1,n):
        inner_xvals.append(f(xvals[i]))

    summ=0
    for i in inner_xvals:
        summ+=i

    integral_approx=(h/2)*((f(xvals[0]))+(2*summ)+f(xvals[-1]))


    return integral_approx

def simpson_rule(f,n,a,b):
    h=(b-a)/n

    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*h)
        xvals.append(xi)

    inner4=[]
    for i in range(1,n,2):
        inner4.append(f(xvals[i]))

    sum_inner4=4*(sum(inner4))

    inner2=[]
    for i in range(2,n-1,2):
        inner2.append(f(xvals[i]))

    sum_inner2=2*(sum(inner2))

    integral_approx=(h/3)*(f(xvals[0]) + sum_inner4 + sum_inner2+ f(xvals[-1]))

    return integral_approx


f=lambda x: (cos(x)*(log(sin(x))))/(sin(x)**2+1)
a=0.1
b=pi/2

nvals=[2]
n=2
while(True):
    n=n*2
    if n>524288:
        break
    nvals.append(n)

list_of_traps=[]
list_of_simpson=[]
for i in nvals:
    trap=trapezoidal_rule(f,i,a,b)
    simp=simpson_rule(f,i,a,b)
    list_of_traps.append(trap)
    list_of_simpson.append(simp)


abs_diff=[]
for i in range(0,len(list_of_simpson)):
    diff=abs(list_of_traps[i]-list_of_simpson[i])
    abs_diff.append(diff)

for i in range(0,len(list_of_simpson)):
    print("{} \t {:.7f} \t {:.7f} \t {:.7f}".format(nvals[i],list_of_traps[i], list_of_simpson[i], abs_diff[i]))







#Question 4:
from math import *
from numpy import *

def trapezoidal_rule(f,n,a,b):
    h=(b-a)/n 
    
    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*((b-a)/n))
        xvals.append(xi)

    inner_xvals=[]
    for i in range (1,n):
        inner_xvals.append(f(xvals[i]))

    summ=0
    for i in inner_xvals:
        summ+=i

    integral_approx=(h/2)*((f(xvals[0]))+(2*summ)+f(xvals[-1]))


    return integral_approx

def simpson_rule(f,n,a,b):
    h=(b-a)/n

    xvals=[]
    for i in range(0,n+1):
        xi=a+(i*h)
        xvals.append(xi)

    inner4=[]
    for i in range(1,n,2):
        inner4.append(f(xvals[i]))

    sum_inner4=4*(sum(inner4))

    inner2=[]
    for i in range(2,n-1,2):
        inner2.append(f(xvals[i]))

    sum_inner2=2*(sum(inner2))

    integral_approx=(h/3)*(f(xvals[0]) + sum_inner4 + sum_inner2+ f(xvals[-1]))

    return integral_approx

f=lambda x: 1/sqrt(1+exp(x)-x)
a=0
b=3
n=2

while True:
    ans=abs(trapezoidal_rule(f,n,a,b)-simpson_rule(f,n,a,b))
    if ans < pow(10,-5):
        break
    n+=2

print(n)






#Question 5:
from math import *
from numpy import *

def midpoint_rule_error(f,n,a,x):
    h=(x-a)/n
    list_of_midpoints=[]
    for i in range(a,n):
        mi=(a+h/2)+(i*h)
        list_of_midpoints.append(mi)

    list_of_fs=[]
    for i in list_of_midpoints:
        integral=f(i)
        list_of_fs.append(integral)

    integral_approx=h*(sum(list_of_fs))
    error=(2/sqrt(pi))*integral_approx
    return error
        

f=lambda t:exp(-t**2)
x=0.5
n=6
a=0
error=midpoint_rule_error(f,n,a,x)
print(error)






#Question 6:
from math import *
from numpy import *

def midpoint_rule_error(f,n,a,x):
    h=(x-a)/n
    list_of_midpoints=[]
    for i in range(a,n):
        mi=(a+h/2)+(i*h)
        list_of_midpoints.append(mi)

    list_of_fs=[]
    for i in list_of_midpoints:
        integral=f(i)
        list_of_fs.append(integral)

    integral_approx=h*(sum(list_of_fs))
    error=(2/sqrt(pi))*integral_approx
    return error
        

        

f=lambda t:exp(-t**2)
x=0.5
n=1
a=0
gauss_error=0.520500

while True:
    midd_err=midpoint_rule_error(f,n,a,x)
    diff=abs(midd_err-gauss_error)
    if diff < pow(10,-6):
        break
    n+=1
h=(x-a)/n
print(h)



