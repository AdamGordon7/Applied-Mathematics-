def bisetion_method(f,a,b):
    
    low=a
    high=b
    count=0

    while(count<=10):
        curr_c=0.5*(low+high)
        count+=1

        if((f(low)*f(curr_c))<0):
            high=curr_c

        else:
            low=curr_c
        
    return curr_c

        

f=lambda x:(x**3) - (x**2) - (4*x) -6
a=1
b=4
print(bisetion_method(f,a,b))

