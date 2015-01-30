x = 25
epsilon = 0.01
ans = x/2.0
n=0
while abs(ans**2-x)>epsilon or n<20:
    if ans**2>x:
        ans = ans/2.0
    else:
        ans = ans + (x-ans)/2
    print ans
    n+=1    
print ans		
