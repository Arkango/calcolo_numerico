import numpy as np
import matploitlib.pyplot as plt

def bisezioni(f,a,b,tol,nmax): #sfrutta punto medio
    x=.5*(a+b) #calcola punto medio
    fa=f(a) #calcola la funzione in a
    fx=f(x) #calcola la funzione in x
    niter = 0 #numero iterazioni iniziale
    res = [] #conterrà il risultato del residuo
    res.append(fx)
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x,fx))
    while .5*(b-a)>tol and niter<nmax:
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        fx=f(x)
        res.append(fx)
        niter+=1
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x,fx)) 
    if .5*(b-a)>tol:
        niter=-1
    return (x,niter,res)


def newton(f,df,x0,tol,nmax):
    niter=0
    err=tol+1
    res = []
    res.append(f(x0))
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x0,err))
    while err>tol and niter<nmax:
        dfx0=df(x0)
        if dfx0 == 0:
            niter=-1
            return(x0,niter)
        fx0=f(x0)
        dx=fx0/dfx0
        x1=x0+dx
        err=abs(dx)
        niter+=1
        res.append(f(x1))
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x1,err))
        x0=x1
    return(x1,niter,res)

def regulafalsi(f,tol,namx):
    while 

def corde():

def secanti():

def quasinewt():


def f(x): return x-np.cos(x)
def df(x): return 1+np.sin(x)

x0=.7
tol=1e-15
namx=100
print('\n\t successive bisezioni \n')
out_bis = bisezioni(f,0,1,tol,nmax)
print('\n\t netwon \n')
out_newt = newton(f,df,x0,tol,nmax)

"""
x_bis = np.arrange(0,out_bis[1]+1)
y_bis= np.array(out_bis[2])
y_bis= np.abs(y_bis)
plt.semilogy(x_bis,y_bis)

x_newt = np.arrange(0,out_newt[1]+1)
y_newt= np.array(out_newt[2])
y_newt= np.abs(y_newt)
plt.semilogy(x_newt,y_newt)
"""