import math as np
def metodo0(f,h,tol,x0,maxIter):
    numIter = 0
    x1 = x0 - ((2 * h)*(f(x0)/(f(x0+h)-f(x0-h))))
    while (x0-x1)/x0 > tol and numIter < maxIter :
        x1= x1 - ((2 * h)*(f(x1)/(f(x1+h)-f(x1-h))))
        numIter +=1
    return(x1,numIter)

def f(x): return np.cos(x) - x**3

print(metodo0(f,10**-6,1e-10,0.85,10))

