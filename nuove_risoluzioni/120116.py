import numpy as np

def radCubic(S,tol,maxIter):
    numIter = 0
    errore = tol+1
    x0 =S
    x1 = S
    valoreFisso = 1/3
    while errore > tol and numIter < maxIter:
        x0 = x1
        x1 = valoreFisso*((2*x0)+(S/x0**2))
        print(x1)
        errore = abs(x0-x1)/abs(x1)
        numIter+=1
    return (x1,numIter)

#print(radCubic(1234,1e-10,20))

def simpson(f,a,b,n):
    h = (b-a)/n
    valoreFisso = h/3
    somma1 = 0
    somma2 = 0
  
    for i in range(1,int((n/2)+1)):
        indice = 2*i -1
        val = f(a+indice*h)
        somma1 += val
    somma1 *= 4
    for i in range(1,int((n/2))):
        indice = 2*i
        val = f(a+indice*h)
        somma2 += val
    somma2 *=2
    somma1 += somma2

    return(valoreFisso*(f(a)+somma1+f(b)))

def f(x): return np.sin(x)

print(simpson(f,0,np.pi,128))