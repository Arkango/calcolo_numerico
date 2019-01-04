import math as np
def metodo0(f,h,tol,x0,maxIter):
    numIter = 0
    x1 = x0 - ((2 * h)*(f(x0)/(f(x0+h)-f(x0-h))))
    
    while ((x0-x1)/x0) < tol and numIter < maxIter :
        x1= x1 - ((2 * h)*(f(x1)/(f(x1+h)-f(x1-h))))
        numIter +=1
    return(x1,numIter)

def f(x): return np.cos(x) - x**3

print(metodo0(f,10**-6,1e-16,0.75,10))



### power method not implemented 'cause numpy not available
 def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new
### 