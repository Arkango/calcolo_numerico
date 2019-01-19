import numpy as np
import matplotlib.pyplot as plt


def lagrange(x,y,u):
    n=x.size
    v=0
    for k in range(0,n):
        L=1
        for j in range(0,n):
            if j != k:
                L=L*(u-x[j])/(x[k]-x[j])
        v=v+y[k]*L
        return v

x=np.array([1,2,3,4,5])
y=np.array([0,1,0,0,0])
s=np.linspace(x[0]-1,x[-1]+1,100)
t=np.zeros(s.size)
for k in range(0,s.size):
    t[k]=lagrange(x,y,s[k])

plt.plot(x,y,'ro')
plt.axis([x[0]-1,x[-1]+1,-1,2])
plt.plot(s,t,'k')
plt.show()