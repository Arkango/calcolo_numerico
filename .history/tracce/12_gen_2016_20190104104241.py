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
    while  (x0-valoreCalcolatO)/x0 < tol and niter < maxIter:       
        x1 = valoreFisso*(2*x0+(s/(x0**2)))
        x0 = x1
        niter += 1
    return(x0,niter)
tol=1e-15
#a = radCubic(1234,tol,20)
#print('valore {:15.10f} niter {:3d} '.format(a[0],a[1]))


def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,n/2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n/2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

def f(x): return mt.sin(x)
sin = simpson(f,0,mt.pi,128)


print(sin)