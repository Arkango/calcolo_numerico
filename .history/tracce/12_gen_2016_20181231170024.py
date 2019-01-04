""" 
input
tol tolleranza
maxIter numero massimo iterate

output
approssimazione di s^1/3
numIter numero di iterate effetuate
"""

import math as mt

def radCubic(s,tol,maxIter):
    if s < 1:
        print('value inserted not correct')
        return False
    x0 = s
    niter = 0
    valoreFisso = float(1)/3
    valoreCalcolatO = x0 ** (1. / 3)
    while  (x0-valoreCalcolatO)/x0 > tol and niter < maxIter:       
        x1 = valoreFisso*(2*x0+(s/(x0**2)))
        x0 = x1
        niter += 1
    return(x0,niter)
tol=1e-15
#a = radCubic(1234,tol,20)
#print('valore {:15.10f} niter {:3d} '.format(a[0],a[1]))


def simpson(f,a,b,n):
    h = (b-a)/n
    x0 = a
    j = 1
    sum1 =0
    sum2 = 0
    enneMezzi = n/2
    while(j < enneMezzi):
        sum1 += f(a+2*j*h)
        sum2 += f(a+2*(j-1)*h)
        j+=1
    sum2 += f(a+2*(enneMezzi-1)*h)
    In = (h/3)*(f(x0)+2*sum1+4*sum2)+f(a+n*h)
    return In
def f(x): return mt.sin(x)
sin = simpson(f,-1,1,4)


print(sin)