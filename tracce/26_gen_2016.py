import numpy as np
def traub(f,dx,x0,tol,maxIter):
    numIter = 0
    dx0 = dx(x0)
    y1 = x0 -(f(x0)/dx0)
    x1 = y1 - (f(y1)/dx0)
    while abs((x0-x1)/x0) > tol and numIter < maxIter:
        x0 = x1
        y1 = x0 -(f(x0)/dx0)
        x1 = y1 - (f(y1)/dx0)
        numIter += 1
    return(x1,numIter)

def f(x): return np.cos(x)-x**3
def dx(x): return -np.sin(x)-3*x**2

x0 = 0.82 
print(traub(f,dx,x0,1e-16,10))