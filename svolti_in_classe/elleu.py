import numpy as np

def elleu(A):
    (m,n)=A.shape
    L=np.eye(n) #inizializzo L
    for k in range(0,n-1):
        if A[k,k] == 0:
            print('pivot in posizione {:1},{:1}'.format(k,k))
            return [],[]
        for i in range(k+1,n):
            L[i,k] = A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j] = A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    return L,U

def elleupp(A):
    (m,n)=A.shape
    p=np.zeros(n-1,dtype=int) #inizializzo p
    L=np.eye(n)
    for k in range(0,n-1):
        r=np.abs(A[k:n,k]).argmax() #cerco valore massimo in valore assoluto
        r=r+k
        p[k]=r
        A[[k,r],:]=A[[r,k],:] #scambio righe di A
        if k>0:
            L[[k,r],0:k]=L[[r,k],0:k] #scambio moltiplicatori
            if A[k,k] == 0:
                print('pivot in posizione {:1},{:1}'.format(k, k))
                return [], [],[],[]
            for i in range(k+1,n):
                L[i,k]=A[i,k]/A[k,k]
                for j in range(k+1,n):
                    A[i,j]=A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    P=np.eye(n)
    for k in range(0,n-1):
        P[[k,p[k]],:]=P[[p[k],k],:]
    return L,U,p,P

""" primo esempio
A=np.array([[-2,-4,-4],[2,-1,0],[4,-2,-4]])
(L,U)=elleu(A.copy())
print(np.dot(L,U)-A)
"""

""" secondo esempio con elleu normale ed errore in x
a=1e-15
A=np.array([[a,1],[1,0]])
b=np.array([[1+a],[1]])
(L,U)=elleu(A.copy())
y=np.linalg.solve(L,b)
x=np.linalg.solve(U,y)
print(x)
"""

""" terzo esempio 
n=100
A=np.random.rand(n,n)
(L,U,p,P)=elleupp(A.copy())
print(np.linalg.norm(np.dot(L,U)-np.dot(P,A)))
"""