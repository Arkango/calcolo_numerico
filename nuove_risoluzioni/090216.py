import numpy as np 

def pow(A,x0,tol,maxIter):
    v0 = 3
    error = tol +1
    numIter = 0
    while error > tol and numIter < maxIter:
        y0 = x0/np.linalg.norm(x0,2)
        x1 = np.dot(A,y0)
        v1 = np.dot(np.transpose(y0),x1)
        x0 = x1
        error = abs(v0-v1)/abs(v1)
        v0 = v1
    return v1
A=np.array([[-0.5,-0.1,0.8],[-0.7,0.1,0],[-0.5,-0.1,0.9]])
x0 = np.array([1,1,1])
print(pow(A,x0,1e-5,10))
