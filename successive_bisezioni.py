# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt

def bisezioni(f,a,b,tol,nmax):
    x=.5*(a+b)
    fa=f(a)
    fx=f(x)
    niter=0
    res =[]
    res.append(fx)
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    while niter < nmax and .5*(b-a) > tol:  
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        fx=f(x)
        res.append(fx)
        niter += 1
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    if .5*(b-a) > tol:
        niter = -1 
    return (x,niter,res)

def newton(f,df,x0,tol,nmax):
    a=3.141592653589793
    niter =0
    err=tol+1
    
    print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    while err>tol and niter<nmax:
        dfx0 = df(x0)
        if dfx0 == 0:
            niter = -1
            return(x0,niter)
        fx0=f(x0)
        dx =-fx0/dfx0
        x1=x0+dx
        err=abs(dx)
        niter+=1
        x0=x1
        print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    return (x0,niter)

def quasinewton(f,x0,tol,nmax):
    a=1.379
    niter =0
    err=tol+1
    h=0.5
    
    print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    while err>tol and niter<nmax:
        dfx0 = (f(x0))/((f(x0+h)-f(x0))/h)
        if dfx0 == 0:
            niter = -1
            return(x0,niter)
        dx =-dfx0
        x1=x0+dx
        err=abs(dx)
        niter+=1
        x0=x1
        print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    return (x0,niter)

def regulafalsi(f,a,b,tol,nmax):
    x= b-(f(a)*(b-a)/(f(b)-f(a)))
    fx= f(x)
    fa=f(a)
    niter = 0
    res =[]
    res.append(fx)
    
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    
    while niter < nmax and b-(f(a)*(b-a)/(f(b)-f(a))) > tol:
        if fx*fa<0:
            b=x
        else:
            a=x
            #fa=fx
        niter+=1
        x= b-(f(a)*(b-a)/(f(b)-f(a)))
        fx= f(x)
        res.append(fx)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    return (x,niter,res)

def corde(f,df,x0,tol,nmax):    
    niter = 0
    fx0=f(x0)
    res =[]
    res.append(fx0)
    err = tol+1
    print('{:2}\t {:1.16f}'.format(niter,x0,fx0))
    while err>tol and niter<nmax:
        dfx0 = df(x0)
        if dfx0 == 0:
            niter = -1
            return(x0,niter)
        fx0=f(x0)
        dx =-(fx0/dfx0)
        x1=x0+dx
        err=abs(dx)
        niter+=1
        x0=x1
        res.append(fx0)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x0,err))
    return (x0,niter,res)
    
def secanti(f,f1,x0,tol,nmax):
    niter = 0
    fx0=f(x0)
    fx1 = f1(x0)
    x1 = x0 - fx0/fx1
    res =[]
    res.append(fx0)
    err = tol+1
    print('{:2}\t {:1.16f}'.format(niter,x0,fx0))
    while err>tol and niter<nmax:
        dfx0 = df(x0)
        if dfx0 == 0:
            niter = -1
            return(x0,niter)
        fx0=f(x0)
        fx1=f(x1)
        x2 = (fx1*x0 - fx0*x1)/(fx1-fx0)
        err=abs(fx1-fx0)
        niter+=1
        x0=x1
        x1=x2
        res.append(fx0)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x0,err))
    return (x0,niter,res)
    

def f(x) : return x**3-(4-x)
def df(x): return 3*(x**2)+1

x0=1
tol=1e-15
nmax = 100
out=quasinewton(f,x0,tol,nmax)





""""
x=np.arange(0,out[1]+1)
y=np.array(out[2])
y=np.abs(y)        
plt.semilogy(y)"""