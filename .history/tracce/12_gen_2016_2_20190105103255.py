import numpy as np
def secanti(f,x0,x1,tol,maxIter):
    numIter = 0
    x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
    while (x0-x1)/x0 > tol and numIter < maxIter:
        x0 = x1
        x1 = x2
        if()
        print(float(f(x1)-f(x0))
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        numIter += 1
    return(x2,numIter)

def f(x): return (np.sin(x)/x)-x 

print(secanti(f,1,0.9,1e-16,10))

