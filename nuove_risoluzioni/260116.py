import numpy as np 
import scipy.linalg as la 

def gaussSeidel(A,b,tol,x0,maxIter):
    numIter =0
    L = np.tril(A)
    U = np.triu(A,1)
    result = x0
    n1x0= np.linalg.norm(x0,1)
    n1result= np.linalg.norm(result,1)
    errore = tol+1
    while  errore> tol and numIter < maxIter:
        x0 = result
        result = la.solve_triangular(L,b-np.dot(U,x0),lower=True)
        numIter += 1
        n1x0= np.linalg.norm(x0,1)
        n1result= np.linalg.norm(result,1)
        errore = abs(n1x0-n1result)/abs(n1result)
    return(result,numIter)

A = np.array([[2.4,-0.8,-0.7],[0.5,1.5,0.7],[-0.1,0.8,2.1]])
#A = np.random.rand(3,3)
b = np.array([0.9,2.7,2.8])
x0 = np.array([2,2,2])
print(gaussSeidel(A,b,1e-5,x0,10))